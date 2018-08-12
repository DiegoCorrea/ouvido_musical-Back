# O.S. and Python/Django Calls
import logging
import pandas as pd
from random import sample
# Application Calls
from apps.kemures.similarities.Cosine.cosine_controller import CosineController
from apps.kemures.similarities.Cosine.cosine_overview import CosineOverview
from apps.kemures.recommenders.UserAverage.user_average_controller import UserAverageController
from apps.metadata.songs.models import Song
from apps.metadata.user_preferences.models import UserPreference
from apps.kemures.kernel_var import SONG_MODEL_SIZE_LIST, TOTAL_RUN

logger = logging.getLogger(__name__)


def one_run_kernel(song_model_size=1500):
    song_model_df = pd.DataFrame.from_records(sample(list(Song.objects.all().values()), song_model_size))
    users_preferences_df = pd.DataFrame.from_records(list(UserPreference.objects.filter(song__in=song_model_df['id'].tolist()).values()))
    if users_preferences_df.empty:
        logger.info("Músicas selecionadas são estão entre as preferencias dos usuarios. Finalizando")
        exit()
    cos = CosineController(song_model_size, song_model_df)
    cos.run_cosine_metadata()
    # logger.info(cos.get_similarity_metadata_df())
    user_ave = UserAverageController(
        similarity_metadata_df=cos.get_similarity_metadata_df(),
        song_model_size=song_model_size,
        song_model_df=song_model_df,
        users_preferences_df=users_preferences_df
    )
    user_ave.run_user_average()
    return user_ave.get_recommendations_df()


def with_config_run_kernel():
    for song_model_size in SONG_MODEL_SIZE_LIST:
        for i in range(TOTAL_RUN):
            song_model_df = pd.DataFrame.from_records(sample(list(Song.objects.all().values()), song_model_size))
            cos = CosineController(song_model_size, song_model_df)
            cos.run_cosine_metadata()
    cos_over = CosineOverview()
    cos_over.make_graphics()
