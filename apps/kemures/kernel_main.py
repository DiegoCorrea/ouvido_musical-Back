# -*- coding: utf-8 -*-
# Python and Pip Modules Calls
import logging
import pandas as pd
from random import sample
# Application Calls
from apps.kemures.similarities.Cosine.cosine_controller import CosineController
from apps.kemures.similarities.Cosine.cosine_overview import CosineOverview
from apps.kemures.recommenders.UserAverage.user_average_controller import UserAverageController
from apps.kemures.recommenders.UserAverage.user_average_overview import UserAverageOverview
from apps.kemures.metrics.MAP.map_controller import MAPController
from apps.kemures.metrics.MAP.map_overview import MAPOverview
from apps.kemures.metrics.MRR.mrr_controller import MRRController
from apps.kemures.metrics.MRR.mrr_overview import MRROverview
from apps.kemures.metrics.NDCG.ndcg_controller import NDCGController
from apps.kemures.metrics.NDCG.ndcg_overview import NDCGOverview
from apps.kemures.analysis_of_recommendations.analysis_of_recommendations import AnalysisOfRecommendations
from apps.metadata.songs.models import Song
from apps.metadata.user_preferences.models import UserPreference
from apps.kemures.kernel_var import SONG_SET_SIZE_LIST, TOTAL_RUN


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
    song_set_df = pd.DataFrame.from_records(sample(list(Song.objects.all().values()), song_set_size))
    users_preferences_df = pd.DataFrame.from_records(
        list(UserPreference.objects.filter(song__in=song_set_df['id'].tolist()).values()))
    users_preferences_df = users_preferences_df.loc[
        users_preferences_df['user_id'].isin(sample(users_preferences_df['user_id'].tolist(), user_set_size))]
    while users_preferences_df.empty:
        song_set_df = pd.DataFrame.from_records(sample(list(Song.objects.all().values()), song_set_size))
        users_preferences_df = pd.DataFrame.from_records(
            list(UserPreference.objects.filter(song__in=song_set_df['id'].tolist()).values()))
        users_preferences_df = users_preferences_df.loc[
            users_preferences_df['user_id'].isin(sample(users_preferences_df['user_id'].tolist(), user_set_size))]
    cos = CosineController(song_set_df=song_set_df)
    cos.run_similarity()
    user_ave = UserAverageController(
        similarity_data_df=cos.get_song_similarity_df(),
        song_set_df=song_set_df,
        users_preferences_df=users_preferences_df
    )
    user_ave.run_recommender()
    an_rec = AnalysisOfRecommendations(
        recommendations_df=user_ave.get_recommendations_df(),
        users_preferences_df=users_preferences_df,
        song_set_df=song_set_df
    )
    an_rec.with_global_song_median()
    map_metric = MAPController(evaluated_recommendations_df=an_rec.get_evaluated_recommendations())
    map_metric.run_for_all_at_size()
    mrr_metric = MRRController(evaluated_recommendations_df=an_rec.get_evaluated_recommendations())
    mrr_metric.run_for_all_at_size()
    ndcg_metric = NDCGController(evaluated_recommendations_df=an_rec.get_evaluated_recommendations())
    ndcg_metric.run_for_all_at_size()


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
            one_run_kernel(song_set_size=song_set_size, user_set_size=100)
    make_graphics()
