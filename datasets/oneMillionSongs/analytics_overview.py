# -*- coding: utf-8 -*-
import os

import pandas as pd


class AnalyticsOverview:
    def __init__(self):
        self.__songs_df = pd.read_csv(os.getcwd() + '/datasets/oneMillionSongs/clean_set/songs.csv')
        self.__users_preferences_df = pd.read_csv(os.getcwd() + '/datasets/oneMillionSongs/clean_set/playCount.csv')
        self.__song_relevance_df = None
        self.__users_df = None
        self.__std_value = 0.0
        self.__max_value = 0.0
        self.__min_value = 0.0

    def print_statistical(self):
        print('Total de usuários: ' + str(self.__users_preferences_df['user_id'].unique().count()))
        print('')
        print('Total de músicas: ' + str(self.__songs_df['id'].count()))
        print('')
        print('Total de álbuns: ' + str(self.__songs_df['album'].unique().count()))
        print('')
        print('Total de Artistas: ' + str(self.__songs_df['artist'].unique().count()))
        print('')
        print('+ Total de músicas preferidas: ' + str(self.__users_preferences_df['song_id'].unique().count()))
        print('+ + Total de Reproduções: ' + str(self.__users_preferences_df['play_count'].sum()))
        print('+ + Música mais preferida: ' + str(self.__max_value))
        print('+ + Música menos preferida: ' + str(self.__min_value))
        print('+ + Desvio Padrão das preferencias: ' + str(self.__std_value))
        print('')

    def __calc_by_songs(self):
        songs_df = pd.DataFrame(columns=['song_id', 'total_play', 'total_liked'])
        for song_id in self.__users_preferences_df['song_id'].unique().tolist():
            df = self.__users_preferences_df.loc[self.__users_preferences_df['song_id'] == song_id]
            songs_df = pd.concat([
                pd.DataFrame(data=[[song_id, sum(df['play_count'].values), df['song_id'].count()]], index=[song_id],
                             columns=['song_id', 'total_play', 'total_liked']),
                songs_df
            ], sort=False)
        return songs_df

    def song_relevance_with_global_like_std(self):
        songs_df = self.__calc_by_songs()
        self.__std_value = songs_df["total_liked"].std()
        self.__max_value = songs_df['total_liked'].max()
        self.__min_value = songs_df['total_liked'].min()
        songs_df['global_relevance_score'] = [total / self.__max_value for total in
                                              songs_df['total_liked'].tolist()]
        song_relevance_id_list = songs_df.loc[
            songs_df['total_liked'] >= self.__std_value, 'song_id'].values
        songs_df['global_relevance'] = [True if x in song_relevance_id_list else False for x in
                                        songs_df['song_id']]
        self.__song_relevance_df = songs_df

    def __calc_by_users(self):
        users_df = pd.DataFrame(columns=['user_id', 'total_play', 'total_liked'])
        for user_id in self.__users_preferences_df['user_id'].unique().tolist():
            df = self.__users_preferences_df.loc[self.__users_preferences_df['user_id'] == user_id]
            users_df = pd.concat([
                pd.DataFrame(data=[[user_id, sum(df['play_count'].values), df['song_id'].count()]], index=[user_id],
                             columns=['song_id', 'total_play', 'total_liked']),
                users_df
            ], sort=False)
        return users_df
