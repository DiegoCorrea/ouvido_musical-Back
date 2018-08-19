# -*- coding: utf-8 -*-
import logging


class HitRecommendations:
    def __init__(self, recommendations_df, song_relevance_df):
        self.__logger = logging.getLogger(__name__)
        self.__recommendations_df = recommendations_df
        self.__song_relevance_df = song_relevance_df

    def get_hited_recommendation_df(self):
        return self.__recommendations_df

    def run(self):
        self.__recommendations_df['global_relevance_score'] = 0.0
        self.__recommendations_df['global_relevance'] = False
        for song_id in self.__song_relevance_df['song_id'].unique().tolist():
            self.__recommendations_df.loc[self.__recommendations_df['song_id'] == song_id, 'global_relevance_score'] = \
                self.__song_relevance_df.at[song_id, 'global_relevance_score']
            self.__recommendations_df.loc[self.__recommendations_df['song_id'] == song_id, 'global_relevance'] = \
                self.__song_relevance_df.at[song_id, 'global_relevance']
