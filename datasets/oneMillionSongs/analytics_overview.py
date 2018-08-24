# -*- coding: utf-8 -*-
import functools
import os
from multiprocessing import Pool as ThreadPool

import matplotlib.pyplot as plt
import pandas as pd

from apps.kemures.kernel.config.global_var import MAX_THREAD


class AnalyticsOverview:
    def __init__(self):
        self.__songs_df = pd.read_csv(os.getcwd() + '/datasets/oneMillionSongs/clean_set/songs.csv')
        self.__users_preferences_df = pd.read_csv(os.getcwd() + '/datasets/oneMillionSongs/clean_set/playCount.csv')
        self.__song_relevance_df = None
        self.__users_relevance_df = None
        self.__users_df = None
        self.__songs_std_value = 0.0
        self.__songs_max_value = 0.0
        self.__songs_min_value = 0.0
        self.__users_std_value = 0.0
        self.__users_max_value = 0.0
        self.__users_min_value = 0.0

    def make_set(self):
        if not os.path.exists(os.getcwd() + '/datasets/oneMillionSongs/set/relevance_set/'):
            os.makedirs(os.getcwd() + '/datasets/oneMillionSongs/set/relevance_set/')
        self.__song_relevance_df.to_csv(os.getcwd() + '/datasets/oneMillionSongs/set/relevance_set/song_relevance.csv')
        self.__users_preferences_df.to_csv(os.getcwd() + '/datasets/oneMillionSongs/set/relevance_set/preferences.csv')
        liked_songs_df = self.__songs_df.loc[self.__songs_df['id'].isin(self.__song_relevance_df['song_id'].tolist())]
        liked_songs_df.to_csv(os.getcwd() + '/datasets/oneMillionSongs/set/relevance_set/songs.csv')
        # self.__users_df.to_csv(os.getcwd() + '/datasets/oneMillionSongs/set/relevance_set/users.csv')

    def print_statistical(self):
        print('Total de usuários: ' + str(self.__users_preferences_df.user_id.unique().size))
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
        print('')

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
        songs_preference_df['global_relevance_score'] = ["{0:.2f}".format(total / self.__songs_max_value) for total in
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

    def calc_a_user(self, user_id):
        print("__ Begin: calc -> user_id: " + str(user_id))
        song_df = self.__users_preferences_df.loc[self.__users_preferences_df['user_id'] == user_id]
        return pd.DataFrame(data=[[user_id, sum(song_df['play_count'].values), song_df['user_id'].count()]],
                            columns=['user_id', 'total_play', 'total_liked'])

    def label_users(self, user_df):
        if user_df['total_liked'] >= self.__users_std_value:
            user_df['global_relevance'] = True
        else:
            user_df['global_relevance'] = False
        user_df['global_relevance_score'] = "{0:.2f}".format(user_df['total_liked'] / self.__users_max_value)
        return user_df

    def __calc_by_users_map(self):
        print("__ Begin: __calc_by_users_map")
        pool = ThreadPool(MAX_THREAD)
        users_preference_df = pool.map(
            self.calc_a_user,
            self.__users_preferences_df['user_id'].unique().tolist()
        )
        pool.close()
        pool.join()
        print("__ End: __calc_by_users_map")
        return pd.concat(users_preference_df, sort=False)

    def user_relevance_with_global_like_std(self):
        users_relevance_df = self.__calc_by_users_map()
        print("__ Begin: user_relevance_with_global_like_std")
        self.__users_std_value = users_relevance_df["total_liked"].std()
        self.__users_max_value = users_relevance_df['total_liked'].max()
        self.__users_min_value = users_relevance_df['total_liked'].min()
        pool = ThreadPool(MAX_THREAD)
        _relevance_df = pd.concat(pool.map(
            self.label_users,
            users_relevance_df
        ), sort=False)
        pool.close()
        pool.join()
        print("__ End: user_relevance_with_global_like_std")
        self.__users_relevance_df = _relevance_df
        self.__users_df = _relevance_df['user_id'].unique()

    def all(self):
        self.song_relevance_with_global_like_std()
        self.make_set()
        self.make_graphics()
        self.print_statistical()

    def make_graphics(self):
        self.song_global_relevance_score_histo()
        self.user_global_relevance_score_histo()

    def song_global_relevance_score_histo(self):
        if not os.path.exists(os.getcwd() + '/files/datasets/oneMillionSongs//'):
            os.makedirs(os.getcwd() + '/files/datasets/oneMillionSongs/')
        plt.figure()
        plt.xlabel('Preferência normalizada')
        plt.ylabel('Quantidade')
        plt.hist(x=self.__song_relevance_df['global_relevance_score'].values.tolist())
        plt.grid(True)
        plt.savefig(
            '/files/datasets/oneMillionSongs/song_global_relevance_score_histo.png'
        )
        plt.close()

    def user_global_relevance_score_histo(self):
        if not os.path.exists(os.getcwd() + '/files/datasets/oneMillionSongs//'):
            os.makedirs(os.getcwd() + '/files/datasets/oneMillionSongs/')
        plt.figure()
        plt.xlabel('Preferência normalizada')
        plt.ylabel('Quantidade')
        plt.hist(x=self.__users_relevance_df['global_relevance_score'].values.tolist())
        plt.grid(True)
        plt.savefig(
            '/files/datasets/oneMillionSongs/user_global_relevance_score_histo.png'
        )
        plt.close()
