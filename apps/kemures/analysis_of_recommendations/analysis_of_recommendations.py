# -*- coding: utf-8 -*-
import logging
from random import choice, uniform
from statistics import median

import pandas as pd


class AnalysisOfRecommendations:
    def __init__(self, recommendations_df, users_preferences_df, song_set_df):
        self.__logger = logging.getLogger(__name__)
        self.__recommendations_df = recommendations_df
        self.__users_preferences_df = users_preferences_df
        self.__song_set_df = song_set_df
        self.__evaluated_recommendations_columns = ['user_id', 'song_id', 'similarity', 'relevance', 'relevance_score']
        self.__evaluated_recommendations_df = recommendations_df

    def with_random_evaluate(self):
        user_recommendations_evaluate_df = pd.DataFrame(columns=self.__evaluated_recommendations_columns)
        for user in self.__recommendations_df['user_id'].unique().tolist():
            __user_recommendation_model = self.__recommendations_df.loc[self.__recommendations_df['user_id'] == user]
            __user_recommendation_model.sort_values(by=['similarity'], ascending=False)
            user_recommendations_df = pd.DataFrame(columns=self.__evaluated_recommendations_columns)
            for (i, row) in __user_recommendation_model.iterrows():
                df = pd.DataFrame(
                    data=[[
                        row['user_id'],
                        row['song_id'],
                        row['similarity'],
                        bool(choice([True, False])),
                        round(uniform(0, 1), 2)
                    ]],
                    columns=self.__evaluated_recommendations_columns,
                )
                user_recommendations_df = pd.concat([user_recommendations_df, df], sort=False)
            user_recommendations_evaluate_df = pd.concat([user_recommendations_evaluate_df, user_recommendations_df],
                                                         sort=False)
        self.__evaluated_recommendations_df = user_recommendations_evaluate_df

    def get_evaluated_recommendations(self):
        return self.__evaluated_recommendations_df

    def __songs_statistical(self):
        songs_df = pd.DataFrame(columns=['song_id', 'total_play', 'total_liked'])
        for song_id in self.__users_preferences_df['song_id'].unique().tolist():
            df = self.__users_preferences_df.loc[self.__users_preferences_df['song_id'] == song_id]
            songs_df = pd.concat([
                pd.DataFrame(data=[[song_id, sum(df['play_count'].values), df['play_count'].count()]], index=[song_id],
                             columns=['song_id', 'total_play', 'total_liked']),
                songs_df
            ], sort=False)
        return songs_df

    def with_global_song_median(self):
        songs_df = self.__songs_statistical()
        median_global_value = median(songs_df['total_play'].tolist())
        max_global_value = max(songs_df['total_play'].tolist())
        songs_df['relevance_score'] = [total_play / max_global_value for total_play in
                                       songs_df['total_play'].tolist()]
        global_relevance_id_list = songs_df.loc[
            songs_df['total_play'] >= median_global_value, 'song_id'].values
        self.__logger.info('Mediana: ' + str(median_global_value))
        self.__logger.info('Total play: ' + str(sum(songs_df['total_play'].tolist())))
        self.__logger.info(global_relevance_id_list)
        self.__evaluated_recommendations_df['relevance'] = [True if x in global_relevance_id_list else False for x in
                                                            self.__recommendations_df[
                                                                'song_id']]
        self.__evaluated_recommendations_df['relevance_score'] = 0.0
        for song_id in songs_df.index.values:
            self.__evaluated_recommendations_df.loc[
                self.__evaluated_recommendations_df['song_id'] == song_id, 'relevance_score'] = songs_df.at[
                song_id, 'relevance_score']

    def with_global_song_std(self):
        songs_df = self.__songs_statistical()
        standard = songs_df["total_liked"].std()
        max_value = songs_df['total_liked'].max()
        songs_df['relevance_score'] = [total / max_value for total in
                                       songs_df['total_liked'].tolist()]
        relevance_songs_id_list = songs_df.loc[
            songs_df['total_liked'] >= standard, 'song_id'].values
        self.__evaluated_recommendations_df['relevance'] = [True if x in relevance_songs_id_list else False for x in
                                                            self.__recommendations_df[
                                                                'song_id']]
        self.__evaluated_recommendations_df['relevance_score'] = 0.0
        for song_id in songs_df.index.values:
            self.__evaluated_recommendations_df.loc[
                self.__evaluated_recommendations_df['song_id'] == song_id, 'relevance_score'] = songs_df.at[
                song_id, 'relevance_score']
        self.__logger.info('Desvio Padrão: ' + str(standard))
        self.__logger.info('Total Liked: ' + str(sum(songs_df['total_liked'].tolist())))
