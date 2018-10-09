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
        self.__recommendations_df = self.__start_user_average_with_async()
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
        self.__logger.info("[Finish Run User Average]")

    def get_user_average_recommendations(self, user_id_list):
        resp_users_recommendation_df = pd.DataFrame()
        for user_id in user_id_list:
            self.__logger.info("[Start Get User Recommendation] - id: " + str(user_id))
            user_model_df = self.__users_preferences_df.loc[self.__users_preferences_df['user_id'] == user_id]
            index_list = user_model_df['song_id'].values.tolist()
            song_model_df = self.__similarity_data_df.loc[index_list]
            song_model_df.drop(columns=index_list)
            # song_model_df = song_model_df.T.drop_duplicates().T
            recommendation_list = {}
            for column in song_model_df.columns:
                column_values = song_model_df[column].values.tolist()
                if len(column_values) == 0:
                    continue
                column_values = [i for i in column_values if i != 0.0]
                if len(column_values) == 0:
                    continue
                similarity = float(sum(column_values)) / float(
                    len(column_values))
                if similarity == 0.0:
                    continue
                recommendation_list[column] = similarity
            user_recommendations_df_list = [pd.DataFrame(
                data=[[user_id, song, recommendation_list[song]]],
                columns=self.__recommendations_columns,
            ) for song in recommendation_list]
            user_recommendations_df = pd.concat(user_recommendations_df_list, sort=False)
            resp_users_recommendation_df = pd.concat(
                [user_recommendations_df.sort_values(by=['similarity'], ascending=False).iloc[
                 0:RECOMMENDATION_LIST_SIZE], resp_users_recommendation_df], sort=False)
        return resp_users_recommendation_df

    def __start_user_average(self):
        pool = ThreadPool(MAX_THREAD)
        users_recommendations_df_list = pool.map(self.get_user_average_recommendations,
                                                 np.array_split(
                                                     self.__users_preferences_df['user_id'].unique(),
                                                     MAX_THREAD))
        pool.close()
        pool.join()
        return pd.concat(users_recommendations_df_list, sort=False)

    def get_user_recommendations(self, user_id):
        self.__logger.info("[Start Get User Recommendation] - id: " + str(user_id))
        user_model_df = self.__users_preferences_df.loc[self.__users_preferences_df['user_id'] == user_id]
        index_list = user_model_df['song_id'].values.tolist()
        song_model_df = self.__similarity_data_df.loc[index_list]
        song_model_df = song_model_df.drop(columns=index_list)
        # song_model_df = song_model_df.T.drop_duplicates().T
        recommendation_list = {}
        for column in song_model_df.columns:
            column_values = song_model_df[column].values.tolist()
            # print('')
            # print('')
            if column in index_list:
                print(column_values)
            column_values = [i for i in column_values if i != 0.0]
            if len(column_values) == 0:
                continue
            similarity = float(sum(column_values)) / float(
                len(column_values))
            if similarity == 0.0:
                continue
            recommendation_list[column] = [similarity]
        user_recommendations_df = pd.DataFrame.from_dict(data=dict(recommendation_list), orient='index',
                                                         columns=['similarity'])
        resp_user_recommendation_df = user_recommendations_df.sort_values(by=['similarity'], ascending=False).iloc[
                                      0:RECOMMENDATION_LIST_SIZE]
        resp_user_recommendation_df['song_id'] = resp_user_recommendation_df.index.values.tolist()
        resp_user_recommendation_df['user_id'] = user_id
        return resp_user_recommendation_df

    def __start_user_average_with_async(self):
        pool = ThreadPool(MAX_THREAD)
        users_recommendations_df_list = pool.map(self.get_user_recommendations,
                                                 self.__users_preferences_df['user_id'].unique().tolist())
        pool.close()
        pool.join()
        resp = pd.concat(users_recommendations_df_list, sort=False)
        resp = resp.reset_index(drop=True)
        # print(resp)
        return resp
