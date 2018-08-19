# -*- coding: utf-8 -*-
import logging

import pandas as pd


class PreferenceStatistics:
    def __init__(self, users_preferences_df):
        self.__logger = logging.getLogger(__name__)
        self.__users_preferences_df = users_preferences_df
        self.__song_relevance_df = None

    def get_song_relevance_df(self):
        return self.__song_relevance_df

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

    def song_relevance_with_global_play_median(self):
        songs_df = self.__calc_by_songs()
        partitioning_value = songs_df['total_play'].median()
        max_value = songs_df['total_play'].max()
        songs_df['global_relevance_score'] = [total / max_value for total in
                                              songs_df['total_play'].tolist()]
        song_relevance_id_list = songs_df.loc[
            songs_df['total_play'] >= partitioning_value, 'song_id'].values
        songs_df['global_relevance'] = [True if x in song_relevance_id_list else False for x in
                                        songs_df['song_id']]
        songs_df['global_relevance_score'] = 0.0
        for song_id in songs_df.index.values:
            songs_df.loc[
                songs_df['song_id'] == song_id, 'global_relevance_score'] = songs_df.at[
                song_id, 'global_relevance_score']
        self.__song_relevance_df = songs_df
        self.__logger.info('Median: ' + str(partitioning_value))
        self.__logger.info('Max: ' + str(max_value))
        self.__logger.info(song_relevance_id_list)

    def song_relevance_with_global_play_std(self):
        songs_df = self.__calc_by_songs()
        partitioning_value = songs_df['total_play'].std()
        max_value = songs_df['total_play'].max()
        songs_df['global_relevance_score'] = [total / max_value for total in
                                              songs_df['total_play'].tolist()]
        song_relevance_id_list = songs_df.loc[
            songs_df['total_play'] >= partitioning_value, 'song_id'].values
        songs_df['global_relevance'] = [True if x in song_relevance_id_list else False for x in
                                        songs_df['song_id']]
        songs_df['global_relevance_score'] = 0.0
        for song_id in songs_df.index.values:
            songs_df.loc[
                songs_df['song_id'] == song_id, 'global_relevance_score'] = songs_df.at[
                song_id, 'global_relevance_score']
        self.__song_relevance_df = songs_df
        self.__logger.info('Median: ' + str(partitioning_value))
        self.__logger.info('Max: ' + str(max_value))
        self.__logger.info(song_relevance_id_list)

    def song_relevance_with_global_like_median(self):
        songs_df = self.__calc_by_songs()
        partitioning_value = songs_df["total_liked"].median()
        max_value = songs_df['total_liked'].max()
        songs_df['global_relevance_score'] = [total / max_value for total in
                                              songs_df['total_liked'].tolist()]
        song_relevance_id_list = songs_df.loc[
            songs_df['total_liked'] >= partitioning_value, 'song_id'].values
        songs_df['global_relevance'] = [True if x in song_relevance_id_list else False for x in
                                        songs_df['song_id']]
        songs_df['global_relevance_score'] = 0.0
        for song_id in songs_df.index.values:
            songs_df.loc[
                songs_df['song_id'] == song_id, 'global_relevance_score'] = songs_df.at[
                song_id, 'global_relevance_score']
        self.__song_relevance_df = songs_df
        self.__logger.info('Standard Deviation: ' + str(partitioning_value))
        self.__logger.info('Max: ' + str(max_value))
        self.__logger.info(song_relevance_id_list)

    def song_relevance_with_global_like_std(self):
        songs_df = self.__calc_by_songs()
        partitioning_value = songs_df["total_liked"].std()
        max_value = songs_df['total_liked'].max()
        songs_df['global_relevance_score'] = [total / max_value for total in
                                              songs_df['total_liked'].tolist()]
        song_relevance_id_list = songs_df.loc[
            songs_df['total_liked'] >= partitioning_value, 'song_id'].values
        songs_df['global_relevance'] = [True if x in song_relevance_id_list else False for x in
                                        songs_df['song_id']]
        songs_df['global_relevance_score'] = 0.0
        for song_id in songs_df.index.values:
            songs_df.loc[
                songs_df['song_id'] == song_id, 'global_relevance_score'] = songs_df.at[
                song_id, 'global_relevance_score']
        self.__song_relevance_df = songs_df
        self.__logger.info('Standard Deviation: ' + str(partitioning_value))
        self.__logger.info('Max: ' + str(max_value))
        self.__logger.info(song_relevance_id_list)
