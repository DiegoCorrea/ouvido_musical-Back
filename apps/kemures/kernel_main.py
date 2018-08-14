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
from apps.kemures.relevance_overview.relevance_overview import RelevanceOverview
from apps.metadata.songs.models import Song
from apps.metadata.user_preferences.models import UserPreference
from apps.kemures.kernel_var import SONG_MODEL_SIZE_LIST, TOTAL_RUN

logger = logging.getLogger(__name__)


def make_graphics():
    cos_over = CosineOverview()
    cos_over.make_graphics()
    user_over = UserAverageOverview()
    user_over.make_graphics()
    map_over = MAPOverview()
    map_over.make_results_graphics()
    map_over.make_time_graphics()
    mrr_over = MRROverview()
    mrr_over.make_results_graphics()
    mrr_over.make_time_graphics()
    ndcg_over = NDCGOverview()
    ndcg_over.make_results_graphics()
    ndcg_over.make_time_graphics()


def one_run_kernel(song_model_size=1500):
    song_model_df = pd.DataFrame.from_records(sample(list(Song.objects.all().values()), song_model_size))
    users_preferences_df = pd.DataFrame.from_records(list(UserPreference.objects.filter(song__in=song_model_df['id'].tolist()).values()))
    while users_preferences_df.empty:
        song_model_df = pd.DataFrame.from_records(sample(list(Song.objects.all().values()), song_model_size))
        users_preferences_df = pd.DataFrame.from_records(
            list(UserPreference.objects.filter(song__in=song_model_df['id'].tolist()).values()))
    cos = CosineController(song_model_size, song_model_df)
    cos.run_cosine_metadata()
    user_ave = UserAverageController(
        similarity_metadata_df=cos.get_similarity_metadata_df(),
        song_model_size=song_model_size,
        song_model_df=song_model_df,
        users_preferences_df=users_preferences_df
    )
    user_ave.run_user_average()
    rel_over = RelevanceOverview(recommendations_df=user_ave.get_recommendations_df())
    rel_over.evaluate_recommendations()
    map_metric = MAPController(evaluated_recommendations_df=rel_over.get_evaluated_recommendations())
    map_metric.run_for_all_at_size()
    mrr_metric = MRRController(evaluated_recommendations_df=rel_over.get_evaluated_recommendations())
    mrr_metric.run_for_all_at_size()
    ndcg_metric = NDCGController(evaluated_recommendations_df=rel_over.get_evaluated_recommendations())
    ndcg_metric.run_for_all_at_size()


def with_config_run_kernel():
    for song_model_size in SONG_MODEL_SIZE_LIST:
        for i in range(TOTAL_RUN):
            logger.info("*" * 30)
            logger.info(
                "*\tTamanho do modelo de músicas ("
                + str(song_model_size)
                + ") Rodada: "
                + str(i)
            )
            logger.info("*" * 30)
            one_run_kernel(song_model_size=song_model_size)
    make_graphics()
