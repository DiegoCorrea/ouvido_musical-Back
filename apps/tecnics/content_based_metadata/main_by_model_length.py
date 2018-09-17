# -*- coding: utf-8 -*-
import logging
from random import sample

import pandas as pd
from django.utils import timezone

from apps.kemures.kernel.config.global_var import SONG_SET_SIZE_LIST, TOTAL_RUN, USER_SIZE
from apps.kemures.kernel.round.models import Round
from apps.kemures.metrics.MAP.map_controller import MAPController
from apps.kemures.metrics.MAP.map_overview import MAPOverview
from apps.kemures.metrics.MRR.mrr_controller import MRRController
from apps.kemures.metrics.MRR.mrr_overview import MRROverview
from apps.kemures.metrics.NDCG.ndcg_controller import NDCGController
from apps.kemures.metrics.NDCG.ndcg_overview import NDCGOverview
from apps.kemures.recommenders.UserAverage.user_average_controller import UserAverageController
from apps.kemures.recommenders.UserAverage.user_average_overview import UserAverageOverview
from apps.kemures.similarities.Cosine.cosine_controller import CosineController
from apps.kemures.similarities.Cosine.cosine_overview import CosineOverview
from apps.metadata.songs.models import Song
from apps.metadata.user_preferences.models import UserPreference
from apps.metadata.user_preferences.preference_statistics import PreferenceStatistics
from apps.tecnics.content_based_metadata.hit_recommendations import HitRecommendations


def make_graphics():
    cos_over = CosineOverview()
    cos_over.make_time_graphics()
    user_over = UserAverageOverview()
    user_over.make_time_graphics()
    map_over = MAPOverview()
    map_over.make_results_graphics()
    map_over.make_time_graphics()
    mrr_over = MRROverview()
    mrr_over.make_results_graphics()
    mrr_over.make_time_graphics()
    ndcg_over = NDCGOverview()
    ndcg_over.make_results_graphics()
    ndcg_over.make_time_graphics()


def one_run_kernel(song_set_size=1500, user_set_size=100):
    song_set_df = pd.DataFrame()
    users_preferences_df = pd.DataFrame()
    while users_preferences_df.empty:
        song_set_df = pd.DataFrame.from_records(sample(list(Song.objects.all().values()), song_set_size))
        users_preferences_df = pd.DataFrame.from_records(
            list(UserPreference.objects.filter(song__in=song_set_df['id'].tolist()).values()))
        users_preferences_df = users_preferences_df.loc[
            users_preferences_df['user_id'].isin(sample(users_preferences_df['user_id'].tolist(), user_set_size))]
    round_instance = Round.objects.create(
        song_set_size=song_set_size,
        user_set_size=user_set_size,
        started_at=timezone.now(),
        finished_at=timezone.now()
    )
    preference_statistic = PreferenceStatistics(
        users_preferences_df=users_preferences_df
    )
    preference_statistic.song_relevance_with_global_play_std()
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


def with_config_run_kernel():
    logger = logging.getLogger(__name__)
    for song_set_size in SONG_SET_SIZE_LIST:
        for i in range(TOTAL_RUN):
            logger.info("*" * 60)
            logger.info(
                "*\tTamanho do modelo de músicas ("
                + str(song_set_size)
                + ") Rodada: "
                + str(i)
            )
            logger.info("*" * 60)
            one_run_kernel(song_set_size=song_set_size, user_set_size=USER_SIZE)
    make_graphics()