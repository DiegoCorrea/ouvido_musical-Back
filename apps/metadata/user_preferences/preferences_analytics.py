# -*- coding: utf-8 -*-
import logging
import os
from collections import Counter
from multiprocessing.dummy import Pool as ThreadPool

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from apps.kemures.kernel.config.global_var import MAX_THREAD

pd.options.display.float_format = '{0:.3}'.format


class PreferenceAnalytics:
    def __init__(self, users_preferences_df, song_df):
        self.__logger = logging.getLogger(__name__)
        self.__users_preferences_df = users_preferences_df
        self.__songs_relevance_df = pd.DataFrame()
        self.__users_relevance_df = pd.DataFrame()
        self.__song_df = song_df
        self.__songs_std_value = 0.0
        self.__songs_max_value = 0.0
        self.__songs_min_value = 0.0
        self.__users_std_value = 0.0
        self.__users_max_value = 0.0
        self.__users_min_value = 0.0
        self.__songs_mean_value = 0.0
        self.__users_mean_value = 0.0
        self.__songs_median_value = 0.0
        self.__users_median_value = 0.0
        self.__path_to_save_graphics = 'files/metadata/'
        if not os.path.exists(self.__path_to_save_graphics):
            os.makedirs(self.__path_to_save_graphics)

    # Users Methods
    def _user_calc(self, users_df):
        for index, row in users_df.iterrows():
            users_df.at[index, 'global_relevance'] = True if row['total_liked'] >= self.__users_std_value else False
        return users_df

    def users_make_global_relevance(self, users_count_df):
        self.__logger.info("__ Begin: users_make_global_relevance")
        pool = ThreadPool(MAX_THREAD)
        users_relevance_df = pool.map(self._user_calc, np.array_split(users_count_df, MAX_THREAD))
        pool.close()
        pool.join()
        self.__logger.info("__ End: users_make_global_relevance")
        return pd.concat(users_relevance_df, sort=False)

    def __user_preference_count(self):
        value_counts = self.__users_preferences_df['user_id'].value_counts()
        resp = value_counts.rename_axis('user_id').reset_index(name='total_liked')
        return resp

    def user_relevance_with_global_like_std(self):
        users_count_df = self.__user_preference_count()
        self.__logger.info("__ Begin: user_relevance_with_global_like_std")
        self.__users_std_value = users_count_df["total_liked"].std()
        self.__users_max_value = users_count_df['total_liked'].max()
        self.__users_min_value = users_count_df['total_liked'].min()
        self.__users_mean_value = users_count_df['total_liked'].mean()
        self.__users_median_value = users_count_df['total_liked'].median()
        users_count_df['global_relevance_score'] = (users_count_df['total_liked'] / self.__users_max_value).values
        self.__users_relevance_df = self.users_make_global_relevance(users_count_df)
        self.__logger.info("__ End: user_relevance_with_global_like_std")

    # Song Methods
    def _song_calc(self, songs_df):
        for index, row in songs_df.iterrows():
            songs_df.at[index, 'global_relevance'] = True if row['total_liked'] >= self.__songs_std_value else False
        return songs_df

    def songs_make_global_relevance(self, songs_count_df):
        self.__logger.info("__ Begin: songs_make_global_relevance")
        pool = ThreadPool(MAX_THREAD)
        songs_relevance_df = pool.map(self._song_calc, np.array_split(songs_count_df, MAX_THREAD))
        pool.close()
        pool.join()
        self.__logger.info("__ End: songs_make_global_relevance")
        return pd.concat(songs_relevance_df, sort=False)

    @staticmethod
    def sum_play_counts(df):

        return pd.DataFrame(data=[df['play_count'].sum()], columns=['total_liked'], index=[df.loc[0, 'song_id']])

    def __song_preference_count(self):
        value_counts = self.__users_preferences_df['song_id'].value_counts()
        resp = value_counts.rename_axis('song_id').reset_index(name='total_liked')
        return resp

    def song_relevance_with_global_like_std(self):
        songs_count_df = self.__song_preference_count()
        self.__logger.info("__ Begin: song_relevance_with_global_like_std")
        self.__songs_std_value = songs_count_df["total_liked"].std()
        self.__songs_max_value = songs_count_df['total_liked'].max()
        self.__songs_min_value = songs_count_df['total_liked'].min()
        self.__songs_mean_value = songs_count_df['total_liked'].mean()
        self.__songs_median_value = songs_count_df['total_liked'].median()
        songs_count_df['global_relevance_score'] = (songs_count_df['total_liked'] / self.__songs_max_value).values
        self.__songs_relevance_df = self.songs_make_global_relevance(songs_count_df)
        self.__songs_relevance_df = self.__songs_relevance_df.set_index('song_id')
        self.__songs_relevance_df['song_id'] = self.__songs_relevance_df.index.values.tolist()
        self.__logger.info("__ End: song_relevance_with_global_like_std")

    # callers
    def run(self):
        self.song_relevance_with_global_like_std()
        self.user_relevance_with_global_like_std()

    def get_users_relevance_preferences_df(self, user_top_n_relevance):
        self.__users_relevance_df.sort_values("global_relevance_score", ascending=False)
        relevance_users = self.__users_relevance_df[:user_top_n_relevance]
        users_relevance_preferences_df = self.__users_preferences_df[
            self.__users_preferences_df['user_id'].isin(relevance_users['user_id'].tolist())]
        return users_relevance_preferences_df

    def get_song_relevance_df(self):
        return self.__songs_relevance_df

    def print_song_statistical(self):
        print('')
        print('+ + Total de músicas: ' + str(self.__songs_relevance_df.song_id.size))
        print('+ + Total de Reproduções: ' + str(self.__users_preferences_df['play_count'].sum()))
        print('+ + Música mais preferida: ' + str(self.__songs_max_value))
        print('+ + Música menos preferida: ' + str(self.__songs_min_value))
        print('+ + Desvio Padrão das preferencias: ' + str(self.__songs_std_value))
        print('- - Desvio Padrão normalizado das preferencias: ' + str(self.__songs_std_value / self.__songs_max_value))
        print('+ + Media das preferencias: ' + str(self.__songs_mean_value))
        print('+ + Mediana das preferencias: ' + str(self.__songs_median_value))
        counted = Counter(self.__songs_relevance_df['global_relevance'].tolist())
        print('+ + Relevância musical: ' + str(counted))
        print('# # Total de Albuns: ' + str(self.__song_df['album'].nunique()))
        print('# # Total de Artists: ' + str(self.__song_df['artist'].nunique()))

    def print_user_statistical(self):
        print('')
        print('- -Total de usuários: ' + str(self.__users_relevance_df.user_id.size))
        print('- - Usuário com mais músicas preferidas: ' + str(self.__users_max_value))
        print('- - Usuário com menos músicas preferidas: ' + str(self.__users_min_value))
        print('- - Desvio Padrão das preferencias: ' + str(self.__users_std_value))
        print('- - Desvio Padrão normalizado das preferencias: ' + str(self.__users_std_value / self.__users_max_value))
        print('+ + Media das preferencias: ' + str(self.__users_mean_value))
        print('+ + Mediana das preferencias: ' + str(self.__users_median_value))
        counted = Counter(self.__users_relevance_df['global_relevance'].tolist())
        print('- - Usuários Relevantes: ' + str(counted))
        print('')

    def song_global_relevance_score_histo(self):
        x = self.__songs_relevance_df.sort_values(by=['global_relevance_score'])
        plt.figure()
        data = x['global_relevance_score'].values.tolist()
        plt.hist(data, bins=100, alpha=0.5,
                 histtype='bar', color='steelblue',
                 edgecolor='black')
        plt.xlabel('Música preferida normalizada')
        plt.ylabel('Quantidade')
        plt.grid(axis='y')
        plt.savefig(
            self.__path_to_save_graphics
            + 'song_global_relevance_score_histo.eps', format='eps', dpi=300
        )
        plt.close()

    def user_global_relevance_score_histo(self):
        x = self.__users_relevance_df.sort_values(by=['global_relevance_score'])
        plt.figure()
        plt.xlabel('Preferência do usuário normalizada')
        plt.ylabel('Quantidade')
        data = x['global_relevance_score'].values.tolist()
        plt.hist(data, bins=100, alpha=0.5,
                 histtype='bar', color='steelblue',
                 edgecolor='black')
        plt.grid(axis='y')
        plt.savefig(
            self.__path_to_save_graphics
            + 'user_global_relevance_score_histo.eps', format='eps', dpi=300
        )
        plt.close()

    def make_graphics(self):
        self.song_global_relevance_score_histo()
        self.user_global_relevance_score_histo()
