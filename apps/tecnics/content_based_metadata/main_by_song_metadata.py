# -*- coding: utf-8 -*-
import logging
from functools import partial
from multiprocessing.dummy import Pool as ThreadPool

import numpy as np
import pandas as pd
from django.utils import timezone

from apps.kemures.kernel.config.global_var import METADATA_TO_PROCESS_LIST, USER_SIZE, MAX_THREAD, \
    METADATA_TO_PROCESS_LIST_PT, USER_SIZE_LIST
from apps.kemures.kernel.round.models import Round
from apps.kemures.metrics.MAP.map_controller import MAPController
from apps.kemures.metrics.MAP.map_overview import MAPOverview
from apps.kemures.metrics.MRR.mrr_controller import MRRController
from apps.kemures.metrics.MRR.mrr_overview import MRROverview
from apps.kemures.metrics.NDCG.ndcg_controller import NDCGController
from apps.kemures.metrics.NDCG.ndcg_overview import NDCGOverview
from apps.kemures.recommenders.UserAverage.user_average_controller import UserAverageController
from apps.kemures.similarities.Cosine.cosine_controller import CosineController
from apps.metadata.songs.models import Song
from apps.metadata.user_preferences.models import UserPreference
from apps.metadata.user_preferences.preference_statistics import PreferenceStatistics
from apps.tecnics.content_based_metadata.hit_recommendations import HitRecommendations


def make_evaluate_graphics(song_size, user_size):
    map_over = MAPOverview()
    map_over.make_graphics_by_metadata(song_size, user_size)
    mrr_over = MRROverview()
    mrr_over.make_graphics_by_metadata(song_size, user_size)
    ndcg_over = NDCGOverview()
    ndcg_over.make_graphics_by_metadata(song_size, user_size)


def get_song_set_df():
    # return pd.DataFrame.from_records(list(Song.objects.all().values()))[:2000]
    return pd.DataFrame.from_records(list(Song.objects.all().values()))


def get_users_preference_df(song_set_df):
    # users_preferences_df = pd.DataFrame.from_records(
    #    list(UserPreference.objects.filter(song__in=song_set_df['id'].tolist()).values())
    # )
    # ids = users_preferences_df['user_id'].unique().tolist()[:2000]
    # return users_preferences_df.loc[users_preferences_df['user_id'].isin(ids)]
    return pd.DataFrame.from_records(
        list(UserPreference.objects.all().values())
    )


def on_map_concat_metadata(df_list, new_column, metadata_to_process_list):
    for index, row in df_list.iterrows():
        new_document = ''
        for metadata in metadata_to_process_list:
            new_document = str(row[metadata]) + ' '
        df_list.at[index, new_column] = new_document
    return df_list


def concat_metadata_preserve_id(df_list, metadata_to_process_list, new_column):
    df_list[new_column] = ''
    pool = ThreadPool(MAX_THREAD)
    new_songs_df = pool.map(partial(on_map_concat_metadata, new_column=new_column,
                                    metadata_to_process_list=metadata_to_process_list),
                            np.array_split(df_list, MAX_THREAD))
    pool.close()
    pool.join()
    resp = pd.concat(new_songs_df, sort=False)
    resp.drop(metadata_to_process_list, axis=1)
    return resp


def one_metadata_process(song_set_df, users_preferences_df, preference_statistic, label):
    round_instance = Round.objects.create(
        metadata_used=label,
        song_set_size=song_set_df['id'].count(),
        user_set_size=users_preferences_df['user_id'].nunique(),
        started_at=timezone.now(),
        finished_at=timezone.now()
    )
    cos_instance = CosineController(
        song_set_df=song_set_df,
        round_instance=round_instance
    )
    cos_instance.run_similarity()
    user_ave_instance = UserAverageController(
        similarity_data_df=cos_instance.get_song_similarity_df(),
        song_set_df=song_set_df,
        users_preferences_df=users_preferences_df,
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


def with_pre_load_data_set():
    logger = logging.getLogger(__name__)
    song_set_df = get_song_set_df()
    preference_statistic = PreferenceStatistics(
        users_preferences_df=get_users_preference_df(song_set_df)
    )
    preference_statistic.run()
    for metadata, pt_graph_name in zip(METADATA_TO_PROCESS_LIST, METADATA_TO_PROCESS_LIST_PT):
        metadata_to_process_list = ['id', metadata]
        logger.info("*" * 60)
        logger.info(
            "*\tProcessando o metadado - "
            + str(metadata)
        )
        logger.info("*" * 60)
        one_metadata_process(song_set_df=song_set_df.filter(metadata_to_process_list, axis=1),
                             users_preferences_df=preference_statistic.get_users_relevance_preferences_df(
                                 user_size=USER_SIZE), preference_statistic=preference_statistic, label=pt_graph_name)
    one_metadata_process(song_set_df=song_set_df.filter(['id', 'album', 'artist'], axis=1),
                         users_preferences_df=preference_statistic.get_users_relevance_preferences_df(
                             user_size=USER_SIZE), preference_statistic=preference_statistic, label='s.AL+s.AR')
    one_metadata_process(
        song_set_df=concat_metadata_preserve_id(df_list=song_set_df, metadata_to_process_list=['album', 'artist'],
                                                new_column='AL+AR'),
        users_preferences_df=preference_statistic.get_users_relevance_preferences_df(
            user_size=USER_SIZE),
        preference_statistic=preference_statistic,
        label='AL+AR')
    preference_statistic.print_song_statistical()
    preference_statistic.print_user_statistical()
    preference_statistic.make_graphics()
    make_evaluate_graphics()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def with_pre_load_data_set_and_user_variation():
    logger = logging.getLogger(__name__)
    song_set_df = get_song_set_df()
    preference_statistic = PreferenceStatistics(
        users_preferences_df=get_users_preference_df(song_set_df)
    )
    preference_statistic.run()
    for user_size in USER_SIZE_LIST:
        for metadata, pt_graph_name in zip(METADATA_TO_PROCESS_LIST, METADATA_TO_PROCESS_LIST_PT):
            metadata_to_process_list = ['id', metadata]
            logger.info("*" * 60)
            logger.info(
                "*\tProcessando o metadado - "
                + str(metadata)
            )
            logger.info("*" * 60)
            one_metadata_process(song_set_df=song_set_df.filter(metadata_to_process_list, axis=1),
                                 users_preferences_df=preference_statistic.get_users_relevance_preferences_df(
                                     user_size=user_size), preference_statistic=preference_statistic,
                                 label=pt_graph_name)
        one_metadata_process(song_set_df=song_set_df.filter(['id', 'album', 'artist'], axis=1),
                             users_preferences_df=preference_statistic.get_users_relevance_preferences_df(
                                 user_size=user_size), preference_statistic=preference_statistic, label='s.AL+s.AR')
        one_metadata_process(
            song_set_df=concat_metadata_preserve_id(df_list=song_set_df, metadata_to_process_list=['album', 'artist'],
                                                    new_column='AL+AR'),
            users_preferences_df=preference_statistic.get_users_relevance_preferences_df(
                user_size=user_size),
            preference_statistic=preference_statistic,
            label='AL+AR')
        preference_statistic.print_song_statistical()
        preference_statistic.print_user_statistical()
        preference_statistic.make_graphics()
        make_evaluate_graphics(song_size=song_set_df['id'].count(), user_size=user_size)


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def data_analysis():
    song_set_df = get_song_set_df()
    preference_statistic = PreferenceStatistics(
        users_preferences_df=get_users_preference_df(song_set_df)
    )
    preference_statistic.run()
    preference_statistic.print_song_statistical()
    preference_statistic.print_user_statistical()
    preference_statistic.make_graphics()
