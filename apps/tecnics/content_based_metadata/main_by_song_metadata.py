# -*- coding: utf-8 -*-
import logging
from functools import partial
from multiprocessing.dummy import Pool as ThreadPool

import numpy as np
import pandas as pd
from django.utils import timezone

from apps.kemures.kernel.config.global_var import METADATA_TO_PROCESS_LIST, USER_SIZE, MAX_THREAD
from apps.kemures.kernel.round.models import Round
from apps.kemures.metrics.MAP.map_controller import MAPController
from apps.kemures.metrics.MAP.map_overview import MAPOverview
from apps.kemures.metrics.MRR.mrr_controller import MRRController
from apps.kemures.metrics.MRR.mrr_overview import MRROverview
from apps.kemures.metrics.NDCG.ndcg_controller import NDCGController
from apps.kemures.recommenders.UserAverage.user_average_controller import UserAverageController
from apps.kemures.similarities.Cosine.cosine_controller import CosineController
from apps.metadata.songs.models import Song
from apps.metadata.user_preferences.models import UserPreference
from apps.metadata.user_preferences.preference_statistics import PreferenceStatistics
from apps.tecnics.content_based_metadata.hit_recommendations import HitRecommendations


def make_graphics():
    map_over = MAPOverview()
    map_over.make_graphics_by_metadata()
    mrr_over = MRROverview()
    mrr_over.make_graphics_by_metadata()
    # ndcg_over = NDCGOverview()
    # ndcg_over.make_graphics_by_metadata()


def get_song_df(metadata_to_process):
    song_set_df = pd.DataFrame.from_records(list(Song.objects.all().values()))
    if isinstance(metadata_to_process, list):
        metadata_to_process.append('id')
        new = song_set_df.filter(metadata_to_process, axis=1)
    else:
        new = song_set_df.filter(['id', metadata_to_process], axis=1)
    # return new[:2000]
    return new


def get_users_preference_df(song_set_df):
    # users_preferences_df = pd.DataFrame.from_records(
    #     list(UserPreference.objects.filter(song__in=song_set_df['id'].tolist()).values())
    # )
    # ids = users_preferences_df['user_id'].unique().tolist()[:2000]
    # return users_preferences_df.loc[users_preferences_df['user_id'].isin(ids)]
    return pd.DataFrame.from_records(
        list(UserPreference.objects.all().values())
    )


def one_run_kernel(metadata_to_process='title', user_set_size=10000):
    song_set_df = get_song_df(metadata_to_process)
    users_preferences_df = get_users_preference_df(song_set_df)
    round_instance = Round.objects.create(
        metadata_used=metadata_to_process,
        song_set_size=song_set_df['id'].count(),
        user_set_size=user_set_size,
        started_at=timezone.now(),
        finished_at=timezone.now()
    )
    preference_statistic = PreferenceStatistics(
        users_preferences_df=users_preferences_df
    )
    preference_statistic.run()
    cos_instance = CosineController(
        song_set_df=song_set_df,
        round_instance=round_instance
    )
    cos_instance.run_similarity()
    user_ave_instance = UserAverageController(
        similarity_data_df=cos_instance.get_song_similarity_df(),
        song_set_df=song_set_df,
        users_preferences_df=preference_statistic.get_users_relevance_preferences_df(user_size=user_set_size),
        round_instance=round_instance
    )
    user_ave_instance.run_recommender()
    hit_rec_instance = HitRecommendations(
        recommendations_df=user_ave_instance.get_recommendations_df(),
        song_relevance_df=preference_statistic.get_song_relevance_df()
    )
    hit_rec_instance.run()
    map_metric = MAPController(
        evaluated_recommendations_df=hit_rec_instance.get_hited_recommendation_df(),
        round_instance=round_instance
    )
    map_metric.run_for_all_at_size()
    mrr_metric = MRRController(
        evaluated_recommendations_df=hit_rec_instance.get_hited_recommendation_df(),
        round_instance=round_instance
    )
    mrr_metric.run_for_all_at_size()
    ndcg_metric = NDCGController(
        evaluated_recommendations_df=hit_rec_instance.get_hited_recommendation_df(),
        round_instance=round_instance
    )
    ndcg_metric.run_for_all_at_size()
    round_instance.finished_at = timezone.now()
    round_instance.save()
    preference_statistic.print_song_statistical()
    preference_statistic.print_user_statistical()


def concat_df(df_list, label, metadata_to_process):
    for index, row in df_list.iterrows():
        df_list.at[index, label] = str(row[metadata_to_process[0]] + ' ' + row[metadata_to_process[1]])
    return df_list


def concat_metadata_df(df_list, metadata_to_process):
    label = str(str(metadata_to_process[0][0]).upper() + str(metadata_to_process[0][1]).upper() + '+' + str(
        metadata_to_process[1][0]).upper() + str(metadata_to_process[1][1]).upper())
    df_list[label] = ''
    pool = ThreadPool(MAX_THREAD)
    songs_relevance_df = pool.map(partial(concat_df, label=label, metadata_to_process=metadata_to_process),
                                  np.array_split(df_list, MAX_THREAD))
    pool.close()
    pool.join()
    return pd.concat(songs_relevance_df, sort=False), label


def get_song_concat_df(metadata_to_process):
    metadata = metadata_to_process
    song_set_df = pd.DataFrame.from_records(list(Song.objects.all().values()))
    if isinstance(metadata_to_process, list):
        metadata.append('id')
        song_df = song_set_df.filter(metadata, axis=1)
    else:
        song_df = song_set_df.filter(['id', metadata], axis=1)
    song_df.set_index('id', drop=False)
    new_df, label = concat_metadata_df(song_df, metadata_to_process)
    new_df.drop(metadata_to_process, axis=1)
    new_df.set_index('id', drop=False)
    return new_df, label


def concat_metadata_run(metadata_to_process, user_set_size=100):
    song_set_df, label = get_song_concat_df(metadata_to_process)
    users_preferences_df = get_users_preference_df(song_set_df)
    round_instance = Round.objects.create(
        metadata_used=label,
        song_set_size=song_set_df['id'].count(),
        user_set_size=user_set_size,
        started_at=timezone.now(),
        finished_at=timezone.now()
    )
    preference_statistic = PreferenceStatistics(
        users_preferences_df=users_preferences_df
    )
    preference_statistic.run()
    cos_instance = CosineController(
        song_set_df=song_set_df,
        round_instance=round_instance
    )
    cos_instance.run_similarity()
    user_ave_instance = UserAverageController(
        similarity_data_df=cos_instance.get_song_similarity_df(),
        song_set_df=song_set_df,
        users_preferences_df=preference_statistic.get_users_relevance_preferences_df(user_size=user_set_size),
        round_instance=round_instance
    )
    user_ave_instance.run_recommender()
    hit_rec_instance = HitRecommendations(
        recommendations_df=user_ave_instance.get_recommendations_df(),
        song_relevance_df=preference_statistic.get_song_relevance_df()
    )
    hit_rec_instance.run()
    map_metric = MAPController(
        evaluated_recommendations_df=hit_rec_instance.get_hited_recommendation_df(),
        round_instance=round_instance
    )
    map_metric.run_for_all_at_size()
    mrr_metric = MRRController(
        evaluated_recommendations_df=hit_rec_instance.get_hited_recommendation_df(),
        round_instance=round_instance
    )
    mrr_metric.run_for_all_at_size()
    ndcg_metric = NDCGController(
        evaluated_recommendations_df=hit_rec_instance.get_hited_recommendation_df(),
        round_instance=round_instance
    )
    ndcg_metric.run_for_all_at_size()
    round_instance.finished_at = timezone.now()
    round_instance.save()
    preference_statistic.print_song_statistical()
    preference_statistic.print_user_statistical()


def with_config_run_kernel():
    logger = logging.getLogger(__name__)
    for metadata in METADATA_TO_PROCESS_LIST:
        logger.info("*" * 60)
        logger.info(
            "*\tProcessando o metadado - "
            + str(metadata)
        )
        logger.info("*" * 60)
        one_run_kernel(metadata_to_process=metadata, user_set_size=USER_SIZE)
    make_graphics()
