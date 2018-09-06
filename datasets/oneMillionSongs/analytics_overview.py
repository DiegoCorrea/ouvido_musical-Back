# -*- coding: utf-8 -*-
import functools
import os
from collections import Counter
from multiprocessing import Pool as ThreadPool

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from apps.kemures.kernel.config.global_var import MAX_THREAD


class AnalyticsOverview:
    def __init__(self):
        self.__songs_df = pd.read_csv(os.getcwd() + '/datasets/oneMillionSongs/clean_set/songs.csv')
        self.__users_preferences_df = pd.read_csv(os.getcwd() + '/datasets/oneMillionSongs/clean_set/playCount.csv')
        # self.__users_preferences_df = self.__users_preferences_df[:1000]
        self.__song_relevance_df = None
        self.__users_relevance_df = None
        self.__users_df = None
        self.__songs_std_value = 0.0
        self.__songs_max_value = 0.0
        self.__songs_min_value = 0.0
        self.__users_std_value = 0.0
        self.__users_max_value = 0.0
        self.__users_min_value = 0.0
        self.__path_to_save_graphics = os.getcwd() + '/files/datasets/oneMillionSongs/'
        self.__path_to_save_set = os.getcwd() + '/datasets/oneMillionSongs/set/relevance_set/'
        if not os.path.exists(self.__path_to_save_set):
            os.makedirs(self.__path_to_save_set)
        if not os.path.exists(self.__path_to_save_graphics):
            os.makedirs(self.__path_to_save_graphics)

    def make_set(self):
        self.__song_relevance_df.to_csv(self.__path_to_save_set + 'song_relevance.csv')
        self.__users_relevance_df.to_csv(self.__path_to_save_set + 'users_relevance.csv')
        self.__users_preferences_df.to_csv(self.__path_to_save_set + 'preferences.csv')
        liked_songs_df = self.__songs_df.loc[self.__songs_df['id'].isin(self.__song_relevance_df['song_id'].tolist())]
        liked_songs_df.to_csv(self.__path_to_save_set + 'songs.csv')
        self.__users_relevance_df.to_csv(self.__path_to_save_set + 'user_relevance.csv')
        self.__users_df.to_csv(self.__path_to_save_set + 'users.csv')

    def print_song_statistical(self):
        print('')
        print('Total de músicas: ' + str(self.__songs_df.id.size))
        print('')
        print('Total de álbuns: ' + str(self.__songs_df.album.unique().size))
        print('')
        print('Total de Artistas: ' + str(self.__songs_df.artist.unique().size))
        print('')
        print('+ Total de músicas preferidas: ' + str(self.__users_preferences_df.song_id.unique().size))
        print('+ + Total de Reproduções: ' + str(self.__users_preferences_df['play_count'].sum()))
        print('+ + Música mais preferida: ' + str(self.__songs_max_value))
        print('+ + Música menos preferida: ' + str(self.__songs_min_value))
        print('+ + Desvio Padrão das preferencias: ' + str(self.__songs_std_value))
        counted = Counter(self.__song_relevance_df['global_relevance'].tolist())
        print('+ + Relevância musical: ' + str(counted))
        print('')
        # print('Total de álbuns: ' + str(self.__song_relevance_df.album.unique().size))
        print('')
        # print('Total de Artistas: ' + str(self.__song_relevance_df.artist.unique().size))
        print('')

    def print_user_statistical(self):
        print('Total de usuários: ' + str(self.__users_df.size))
        print('')
        print('+ + Usuário com mais músicas preferidas: ' + str(self.__users_max_value))
        print('+ + Usuário com menos músicas preferidas: ' + str(self.__users_min_value))
        print('+ + Desvio Padrão das preferencias: ' + str(self.__users_std_value))
        counted = Counter(self.__users_relevance_df['global_relevance'].tolist())
        print('+ + Usuários Relevantes: ' + str(counted))

    def calc_a_song(self, song_id):
        print("__ Begin: calc -> song_id: " + str(song_id))
        song_df = self.__users_preferences_df.loc[self.__users_preferences_df['song_id'] == song_id]
        return pd.DataFrame(data=[[song_id, sum(song_df['play_count'].values), song_df['song_id'].count()]],
                            columns=['song_id', 'total_play', 'total_liked'])

    def __calc_by_songs_map(self):
        print("__ Begin: __calc_by_songs_map")
        pool = ThreadPool(MAX_THREAD)
        songs_preference_df = pool.map(
            self.calc_a_song,
            self.__users_preferences_df['song_id'].unique().tolist()
        )
        pool.close()
        pool.join()
        print("__ End: __calc_by_songs_map")
        return pd.concat(songs_preference_df, sort=False)

    def make_relevance_vector(self, y, x):
        return True if x in y else False

    def song_relevance_with_global_like_std(self):
        print("__ Begin: song_relevance_with_global_like_std")
        songs_preference_df = self.__calc_by_songs_map()
        self.__songs_std_value = songs_preference_df["total_liked"].std()
        self.__songs_max_value = songs_preference_df['total_liked'].max()
        self.__songs_min_value = songs_preference_df['total_liked'].min()
        songs_preference_df['global_relevance_score'] = ["{0:.5f}".format(total / self.__songs_max_value) for total in
                                                         songs_preference_df['total_liked'].tolist()]
        song_relevance_id_list = songs_preference_df.loc[
            songs_preference_df['total_liked'] >= self.__songs_std_value, 'song_id'].values
        pool = ThreadPool(MAX_THREAD)
        songs_preference_df['global_relevance'] = pool.map(
            functools.partial(
                self.make_relevance_vector,
                song_relevance_id_list
            ),
            songs_preference_df['song_id'].tolist()
        )
        pool.close()
        pool.join()
        print("__ Begin: song_relevance_with_global_like_std")
        self.__song_relevance_df = songs_preference_df

    # Users Methods
    def __calc_by_users_map(self):
        print("__ Begin: __calc_by_users_map")
        users_id_list_splitted = np.array_split(np.array(self.__users_preferences_df['user_id'].unique().tolist()),
                                                MAX_THREAD)
        pool = ThreadPool(MAX_THREAD)
        users_preference_df = pool.map(
            self.user_preference_count,
            users_id_list_splitted
        )
        pool.close()
        pool.join()
        print("__ End: __calc_by_users_map")
        return pd.concat(users_preference_df, sort=False)

    def user_preference_count(self, users_id_list):
        users_relevance_df = pd.DataFrame()
        for user_id in users_id_list:
            # print('__ Begin user_preference_count: ' + str(user_id))
            user_df = self.__users_preferences_df.loc[self.__users_preferences_df['user_id'] == user_id]
            users_relevance_df = pd.concat([
                users_relevance_df,
                pd.DataFrame(data=[[user_id, sum(user_df['play_count'].values), user_df['user_id'].count()]],
                             columns=['user_id', 'total_play', 'total_liked'], index=[user_id])
            ])
        return users_relevance_df

    def _user_calc(self, users_df):
        print("__ Begin: _user_calc")
        for index, row in users_df.iterrows():
            # print('index: ', str(index))
            users_df.at[index, 'global_relevance'] = True if row['total_liked'] >= self.__users_std_value else False
            users_df.at[index, 'global_relevance_score'] = "{0:.5f}".format(row['total_liked'] / self.__users_max_value)
        return users_df

    def users_make_global_relevance(self, users_relevance_df):
        users_relevance_df_split = np.array_split(users_relevance_df, MAX_THREAD)
        pool = ThreadPool(MAX_THREAD)
        users_relevance_df = pool.map(self._user_calc, users_relevance_df_split)
        pool.close()
        pool.join()
        return pd.concat(users_relevance_df, sort=False)

    def user_relevance_with_global_like_std(self):
        users_relevance_df = self.__calc_by_users_map()
        print("__ Begin: user_relevance_with_global_like_std")
        self.__users_std_value = users_relevance_df["total_liked"].std()
        self.__users_max_value = users_relevance_df['total_liked'].max()
        self.__users_min_value = users_relevance_df['total_liked'].min()
        self.__users_relevance_df = self.users_make_global_relevance(users_relevance_df)

        self.__users_df = pd.DataFrame(data=self.__users_relevance_df['user_id'].unique().tolist(),
                                       columns=['user_id'])
        print("__ End: user_relevance_with_global_like_std")

    def all(self):
        self.song_check()
        self.user_check()
        self.make_set()

    def song_check(self):
        self.song_relevance_with_global_like_std()
        self.song_global_relevance_score_histo()
        self.print_song_statistical()

    def user_check(self):
        self.user_relevance_with_global_like_std()
        self.user_global_relevance_score_histo()
        self.print_user_statistical()

    def song_global_relevance_score_histo(self):
        x = self.__song_relevance_df.sort_values(by=['global_relevance_score'])
        plt.figure()
        data = x['global_relevance_score'].values.tolist()
        plt.hist(data, bins=30, alpha=0.5,
                 histtype='stepfilled', color='steelblue',
                 edgecolor='none')
        plt.xlabel('Música preferida normalizada')
        plt.ylabel('Quantidade')
        plt.grid(axis='y')
        plt.savefig(
            self.__path_to_save_graphics
            + 'song_global_relevance_score_histo.png'
        )
        plt.close()

    def user_global_relevance_score_histo(self):
        x = self.__users_relevance_df.sort_values(by=['global_relevance_score'])
        plt.figure()
        plt.xlabel('Preferência do usuário normalizada')
        plt.ylabel('Quantidade')
        data = x['global_relevance_score'].values.tolist()
        plt.hist(data, bins=30, alpha=0.5,
                 histtype='stepfilled', color='steelblue',
                 edgecolor='none')
        plt.grid(axis='y')
        plt.savefig(
            self.__path_to_save_graphics
            + 'user_global_relevance_score_histo.png'
        )
        plt.close()
