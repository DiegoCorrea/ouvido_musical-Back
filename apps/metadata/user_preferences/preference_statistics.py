# -*- coding: utf-8 -*-
import logging
from multiprocessing.dummy import Pool as ThreadPool

import numpy as np
import pandas as pd

from apps.kemures.kernel.config.global_var import MAX_THREAD


class PreferenceStatistics:
    def __init__(self, users_preferences_df):
        self.__logger = logging.getLogger(__name__)
        self.__users_preferences_df = users_preferences_df
        self.__songs_relevance_df = pd.DataFrame()
        self.__users_relevance_df = pd.DataFrame()
        self.__songs_std_value = 0.0
        self.__songs_max_value = 0.0
        self.__songs_min_value = 0.0
        self.__users_std_value = 0.0
        self.__users_max_value = 0.0
        self.__users_min_value = 0.0

    # Users Methods
    def user_preference_count(self, users_id_list):
        users_relevance_df = pd.DataFrame()
        for user_id in users_id_list:
            user_df = self.__users_preferences_df.loc[self.__users_preferences_df['user_id'] == user_id]
            users_relevance_df = pd.concat([
                users_relevance_df,
                pd.DataFrame(data=[[user_id, sum(user_df['play_count'].values), user_df['user_id'].count()]],
                             columns=['user_id', 'total_play', 'total_liked'], index=[user_id])
            ])
        return users_relevance_df

    def __calc_by_users_map(self):
        self.__logger.info("__ Begin: __calc_by_users_map")
        users_id_split_list = np.array_split(np.array(self.__users_preferences_df['user_id'].unique().tolist()),
                                             MAX_THREAD)
        pool = ThreadPool(MAX_THREAD)
        users_preference_df = pool.map(
            self.user_preference_count,
            users_id_split_list
        )
        pool.close()
        pool.join()
        self.__logger.info("__ End: __calc_by_users_map")
        return pd.concat(users_preference_df, sort=False)

    def _user_calc(self, users_df):
        for index, row in users_df.iterrows():
            users_df.at[index, 'global_relevance'] = True if row['total_liked'] >= self.__users_std_value else False
            users_df.at[index, 'global_relevance_score'] = "{0:.3f}".format(row['total_liked'] / self.__users_max_value)
        return users_df

    def users_make_global_relevance(self, users_count_df):
        self.__logger.info("__ Begin: users_make_global_relevance")
        users_relevance_df_split = np.array_split(users_count_df, MAX_THREAD)
        pool = ThreadPool(MAX_THREAD)
        users_relevance_df = pool.map(self._user_calc, users_relevance_df_split)
        pool.close()
        pool.join()
        self.__logger.info("__ End: users_make_global_relevance")
        return pd.concat(users_relevance_df, sort=False)

    def user_relevance_with_global_like_std(self):
        users_count_df = self.__calc_by_users_map()
        self.__logger.info("__ Begin: user_relevance_with_global_like_std")
        self.__users_std_value = users_count_df["total_liked"].std()
        self.__users_max_value = users_count_df['total_liked'].max()
        self.__users_min_value = users_count_df['total_liked'].min()
        self.__users_relevance_df = self.users_make_global_relevance(users_count_df)
        self.__logger.info("__ End: user_relevance_with_global_like_std")

    # Song Methods
    def _song_preference_count_df(self, song_id):
        print("----> " + str(song_id))
        song_df = self.__users_preferences_df.loc[self.__users_preferences_df['song_id'] == song_id]
        return pd.DataFrame(data=[[song_id, sum(song_df['play_count'].values), song_df['song_id'].count()]],
                            columns=['song_id', 'total_play', 'total_liked'], index=[song_id])

    def song_preference_count(self, song_id):
        print("----> " + str(song_id))
        song_df = self.__users_preferences_df.loc[self.__users_preferences_df['song_id'] == song_id]
        return [song_id, sum(song_df['play_count'].values), song_df['song_id'].count()]

    def _song_preference_count_list(self, songs_id_list):
        songs_relevance_df = pd.DataFrame()
        for song_id in songs_id_list:
            print("----> " + str(song_id))
            song_df = self.__users_preferences_df.loc[self.__users_preferences_df['song_id'] == song_id]
            songs_relevance_df = pd.concat([
                songs_relevance_df,
                pd.DataFrame(data=[[song_id, sum(song_df['play_count'].values), song_df['song_id'].count()]],
                             columns=['song_id', 'total_play', 'total_liked'], index=[song_id])
            ])
        return songs_relevance_df

    def __count_by_songs_map(self):
        self.__logger.info("__ Begin: __count_by_songs_map")
        # songs_id_split_list = np.array_split(np.array(self.__users_preferences_df['song_id'].unique().tolist()),
        #                                      MAX_THREAD)
        pool = ThreadPool(MAX_THREAD)
        songs_preference_df = pool.map(
            self.song_preference_count,
            self.__users_preferences_df['song_id'].unique().tolist()
        )
        pool.close()
        pool.join()
        self.__logger.info("__ End: __count_by_songs_map")
        return pd.DataFrame(data=songs_preference_df, columns=['song_id', 'total_play', 'total_liked'])

    def _song_calc(self, songs_df):
        for index, row in songs_df.iterrows():
            songs_df.at[index, 'global_relevance'] = True if row['total_liked'] >= self.__songs_std_value else False
            songs_df.at[index, 'global_relevance_score'] = "{0:.3f}".format(row['total_liked'] / self.__songs_max_value)
        return songs_df

    def songs_make_global_relevance(self, songs_count_df):
        self.__logger.info("__ Begin: songs_make_global_relevance")
        songs_relevance_df_split = np.array_split(songs_count_df, MAX_THREAD)
        pool = ThreadPool(MAX_THREAD)
        songs_relevance_df = pool.map(self._song_calc, songs_relevance_df_split)
        pool.close()
        pool.join()
        self.__logger.info("__ End: songs_make_global_relevance")
        return pd.concat(songs_relevance_df, sort=False)

    def song_relevance_with_global_like_std(self):
        songs_count_df = self.__count_by_songs_map()
        self.__logger.info("__ Begin: song_relevance_with_global_like_std")
        self.__songs_std_value = songs_count_df["total_liked"].std()
        self.__songs_max_value = songs_count_df['total_liked'].max()
        self.__songs_min_value = songs_count_df['total_liked'].min()
        self.__songs_relevance_df = self.songs_make_global_relevance(songs_count_df)
        self.__logger.info("__ End: song_relevance_with_global_like_std")

    # callers
    def run(self):
        self.song_relevance_with_global_like_std()
        self.user_relevance_with_global_like_std()

    def get_users_relevance_preferences_df(self, user_size):
        self.__users_relevance_df.sort_values("global_relevance")
        return self.__users_relevance_df[:user_size]

    def get_song_relevance_df(self):
        return self.__songs_relevance_df
