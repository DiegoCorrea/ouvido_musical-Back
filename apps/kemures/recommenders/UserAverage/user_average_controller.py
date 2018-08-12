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
    RECOMMENDATION_LIST_SIZE
)
logger = logging.getLogger(__name__)


class UserAverageController:
    def __init__(self, similarity_metadata_df, song_model_size, song_model_df, users_preferences_df):
        self.similarity_metadata_df = similarity_metadata_df
        self.song_model_size = song_model_size
        self.life = UserAverageLife.objects.create(song_model_size=song_model_size)
        self.recommendations_columns = ['user_id', 'song_id', 'similarity', 'iLike', 'score']
        self.recommendations_df = pd.DataFrame(columns=self.recommendations_columns)
        self.song_model_df = song_model_df
        self.users_preferences_df = users_preferences_df
        self.user_list = users_preferences_df['user_id'].unique().tolist()

    def get_recommendations_df(self):
        return self.recommendations_df

    def run_user_average(self):
        logger.info("[Start Run User Average]")
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
        logger.info("[Start Run User Average]")

    def get_user_average_recommendations(self, user):
        logger.info("[Start Get User Recommendation] - id: " + str(user))
        __user_model_df = self.users_preferences_df.loc[self.users_preferences_df['user_id'] == user]
        __song_model_df = self.song_model_df.loc[~self.song_model_df['id'].isin(__user_model_df['song_id'])]
        __user_similar_songs_df = self.similarity_metadata_df.loc[__user_model_df['song_id'].tolist()]
        # logger.info(__user_similar_songs_df)
        recommendation_list = {}
        for column in __user_similar_songs_df.columns:
            similarity = float(sum(__user_similar_songs_df[column].tolist()))/float(__user_similar_songs_df[column].count())
            if similarity == 0.0:
                continue
            recommendation_list[column] = similarity
        # logger.info(recommendation_list)
        user_recommendations_df = pd.DataFrame(columns=self.recommendations_columns)
        for song in recommendation_list:
            df = pd.DataFrame(
                data=[[user, song, recommendation_list[song], True, 1]],
                columns=self.recommendations_columns,
            )
            #logger.info(df)
            user_recommendations_df = pd.concat([user_recommendations_df, df], sort=False)
        return user_recommendations_df

    def __start_user_average(self):
        logger.info("[Start User Average]")
        pool = ThreadPool(MAX_THREAD)
        users_recommendations_df = pool.map(self.get_user_average_recommendations, self.user_list[:20])
        pool.close()
        pool.join()
        recommendations_df = pd.DataFrame(columns=self.recommendations_columns)
        for df in users_recommendations_df:
            recommendations_df = pd.concat([recommendations_df, df], sort=False)
        logger.info("[Finish User Average]")
        return recommendations_df
