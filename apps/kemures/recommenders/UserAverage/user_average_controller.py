# -*- coding: utf-8 -*-
import logging
from multiprocessing.dummy import Pool as ThreadPool

import numpy as np
import pandas as pd
from django.utils import timezone

from apps.kemures.kernel.config.global_var import (
    MAX_THREAD,
    RECOMMENDATION_LIST_SIZE
)
from apps.kemures.recommenders.UserAverage.runtime.models import UserAverageRunTime


class UserAverageController:
    def __init__(self, similarity_data_df, users_preferences_df, round_instance):
        self.__logger = logging.getLogger(__name__)
        self.__similarity_data_df = similarity_data_df
        self.__round_instance = round_instance
        self.__recommendations_columns = ['user_id', 'song_id', 'similarity']
        self.__recommendations_df = pd.DataFrame(columns=self.__recommendations_columns)
        self.__users_preferences_df = users_preferences_df

    def get_recommendations_df(self):
        return self.__recommendations_df

    def run_recommender(self):
        self.__logger.info("[Start Run User Average]")
        started_at = timezone.now()
        self.__recommendations_df = self.__start_user_average()
        finished_at = timezone.now()
        UserAverageRunTime.objects.create(
            round=self.__round_instance,
            started_at=started_at,
            finished_at=finished_at
        )
        self.__logger.info(
            "User Average Run Time: Start at - "
            + str(started_at)
            + " || Finished at -"
            + str(finished_at)
        )
        self.__logger.info("[Start Run User Average]")

    def get_user_average_recommendations(self, user_id_list):
        resp_users_recommendation_df = pd.DataFrame()
        for user_id in user_id_list:
            self.__logger.info("[Start Get User Recommendation] - id: " + str(user_id))
            user_model_df = self.__users_preferences_df.loc[self.__users_preferences_df['user_id'] == user_id]
            song_model_df = self.__similarity_data_df.loc[user_model_df['song_id'].tolist()]
            index_list = song_model_df.index.values.tolist()
            song_model_df.drop(columns=index_list)
            recommendation_list = {}
            for column in song_model_df.columns:
                if column in index_list:
                    continue
                similarity = float(sum(song_model_df[column].tolist())) / float(
                    song_model_df[column].count())
                if similarity == 0.0:
                    continue
                recommendation_list[column] = similarity
            user_recommendations_df = pd.DataFrame(columns=self.__recommendations_columns)
            for song in recommendation_list:
                user_recommendations_df = pd.concat([user_recommendations_df, pd.DataFrame(
                    data=[[user_id, song, recommendation_list[song]]],
                    columns=self.__recommendations_columns,
                )], sort=False)
            resp_users_recommendation_df = pd.concat(
                [user_recommendations_df.sort_values(by=['similarity'], ascending=False).iloc[
                 0:RECOMMENDATION_LIST_SIZE], resp_users_recommendation_df], sort=False)
        return resp_users_recommendation_df

    def __start_user_average(self):
        pool = ThreadPool(MAX_THREAD)
        users_recommendations_df_list = pool.map(self.get_user_average_recommendations,
                                                 np.array_split(
                                                     self.__users_preferences_df['user_id'].unique().tolist(),
                                                     MAX_THREAD))
        pool.close()
        pool.join()
        return pd.concat(users_recommendations_df_list, sort=False)
