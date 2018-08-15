import logging
from random import choice, uniform
import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)


class RelevanceOverview:
    def __init__(self, recommendations_df):
        self.recommendations_df = recommendations_df
        self.evaluated_recommendations_columns = ['user_id', 'song_id', 'similarity', 'iLike', 'score']
        self.evaluated_recommendations_df = pd.DataFrame(columns=self.evaluated_recommendations_columns)

    def evaluate_recommendations(self):
        user_recommendations_evaluate_df = pd.DataFrame(columns=self.evaluated_recommendations_columns)
        for user in self.recommendations_df['user_id'].unique().tolist():
            __user_recommendation_model = self.recommendations_df.loc[self.recommendations_df['user_id'] == user]
            __user_recommendation_model.sort_values(by=['similarity'], ascending=False)
            user_recommendations_df = pd.DataFrame(columns=self.evaluated_recommendations_columns)
            for (i, row) in __user_recommendation_model.iterrows():
                df = pd.DataFrame(
                    data=[[
                        row['user_id'],
                        row['song_id'],
                        row['similarity'],
                        bool(choice([True, False])),
                        round(uniform(0, 1), 2)
                    ]],
                    columns=self.evaluated_recommendations_columns,
                )
                user_recommendations_df = pd.concat([user_recommendations_df, df], sort=False)
            user_recommendations_evaluate_df = pd.concat([user_recommendations_evaluate_df, user_recommendations_df],
                                                         sort=False)
        self.evaluated_recommendations_df = user_recommendations_evaluate_df

    def get_evaluated_recommendations(self):
        return self.evaluated_recommendations_df
