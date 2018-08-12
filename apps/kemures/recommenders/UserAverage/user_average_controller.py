# -*- coding: utf-8 -*-
# O.S. and Python/Django Calls
import logging
from django.utils import timezone
from multiprocessing import Pool as ThreadPool
# Modules Calls
import pandas as pd
# Application Calls
from apps.kemures.recommenders.UserAverage.DAO.models import UserAverageRecommendations, UserAverageLife
from apps.kemures.recommenders.UserAverage.runtime.models import UserAverageRunTime
from apps.kemures.kernel_var import (
    MAX_THREAD,
)
logger = logging.getLogger(__name__)


class UserAverageController:
    def __init__(self, similarity_metadata_df, song_model_size, song_model_df, users_preferences_df):
        self.similarity_metadata_df = similarity_metadata_df
        self.song_model_size = song_model_size
        self.life = None
        self.recommendations_df = pd.DataFrame()
        self.song_model_df = song_model_df
        self.users_preferences_df = users_preferences_df
        self.user_list = users_preferences_df['user_id'].unique().tolist()

    def run_user_average(self):
        logger.info("[Start Run User Average - Benchmark]")
        started_at = timezone.now()
        self.recommendations_df = self.__start_user_average()
        finished_at = timezone.now()
        UserAverageRunTime.objects.create(
            life=self.life,
            song_model_size=self.song_model_size,
            started_at=started_at,
            finished_at=finished_at
        )
        logger.info(
            "Benchmark: Start at - "
            + str(started_at)
            + " || Finished at -"
            + str(finished_at)
        )
        logger.info("[Start Run User Average] - Benchmark")

    def get_user_average_recommendations(self, user):
        logger.info("[Start Get User Recommendation] - id: " + str(user))
        __user_model_df = self.users_preferences_df.loc[self.users_preferences_df['user_id'] == user]
        __song_model_df = self.song_model_df.loc[~self.song_model_df['id'].isin(__user_model_df['song_id'])]
        __similar_df = self.similarity_metadata_df.loc[__user_model_df['song_id'].tolist()]

    def __start_user_average(self):
        logger.info("[Start User Average]")
        self.life = UserAverageLife.objects.create(song_model_size=self.song_model_size)
        pool = ThreadPool(MAX_THREAD)
        user_recommendations_df = pool.map(self.get_user_average_recommendations, self.user_list)
        pool.close()
        pool.join()
        logger.info("[Finish User Average]")
        return user_recommendations_df
