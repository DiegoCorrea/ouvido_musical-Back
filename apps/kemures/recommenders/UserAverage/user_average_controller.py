# -*- coding: utf-8 -*-
# O.S. and Python/Django Calls
import logging
from django.utils import timezone
from multiprocessing import Pool as ThreadPool
# Modules Calls
import pandas as pd
# Application Calls
from apps.kemures.recommenders.UserAverage.DAO.models import UserAverageRecommendations, UserAverageLife
from apps.kemures.recommenders.UserAverage.runtime.models import UserAverageRunTime
from apps.kemures.kernel_var import (
    MAX_THREAD,
)
logger = logging.getLogger(__name__)


class UserAverageController:
    def __init__(self, similarity_metadata_df, song_model_size, song_model_df, users_preferences_df):
        self.similarity_metadata_df = similarity_metadata_df
        self.song_model_size = song_model_size
        self.life = None
        self.recommendations_df = pd.DataFrame()
        self.song_model_df = song_model_df
        self.users_preferences_df = users_preferences_df

    def run_user_average(self):
        logger.info("[Start Run User Average - Benchmark]")
        started_at = timezone.now()
        self.recommendations_df = self.__start_user_average()
        finished_at = timezone.now()
        UserAverageRunTime.objects.create(
            life=self.life,
            started_at=started_at,
            finished_at=finished_at
        )
        logger.info(
            "Benchmark: Start at - "
            + str(started_at)
            + " || Finished at -"
            + str(finished_at)
        )
        logger.info("[Start Run User Average] - Benchmark")

    def __get_user_average_recommendations(self, user):
        logger.info("[Start Get User Recommendation] - id: " + str(user))
        __user_model_df = self.users_preferences_df.loc[self.users_preferences_df['user_id'] == user]
        __song_model_df = self.song_model_df.loc[self.song_model_df['id'] == __user_model_df['song_id'].tolist()]
        for user_preference in __user_model_df:
            base = __song_model_df.index.get_indexer_for((__song_model_df[__song_model_df.id == user_preference['song_id']].index))
            similaresSide = songPlayed.song.getSimilaries(songIDList=userModel)
            for songSimi in similaresSide:
                if songSimi.similarity == 0.0:
                    continue
                if songSimi.songBase == songPlayed.song:
                    if songSimi.songCompare in recommendations:
                        recommendations[songSimi.songCompare].append(
                            songSimi.similarity
                        )
                    else:
                        recommendations.setdefault(songSimi.songCompare, [])
                        recommendations[songSimi.songCompare].append(
                            songSimi.similarity
                        )
                else:
                    if songSimi.songBase in recommendations:
                        recommendations[songSimi.songBase].append(
                            songSimi.similarity
                        )
                    else:
                        recommendations.setdefault(songSimi.songBase, [])
                        recommendations[songSimi.songBase].append(
                            songSimi.similarity
                        )
        rec = {}
        for (song, values) in recommendations.items():
            rec.setdefault(song, sum(values) / len(values))
        orderedRecomendation = sorted(
            rec.items(),
            key=lambda t: t[1],
            reverse=True
        )[:RECOMMENDATION_LIMIT]
        with transaction.atomic():
            for (song, similarity) in orderedRecomendation:
                try:
                    UserAverage_Recommendations.objects.create(
                        song_id=song.id,
                        user_id=user.id,
                        life_id=RECOMMENDATION_CONFIG['LIFE_ID'],
                        similarity=similarity,
                        iLike=bool(choice([True, False])),
                        score=randint(MIN_SCORE, MAX_SCORE))
                except Exception as e:
                    logger.error(str(e))
                    continue

    def __start_user_average(self):
        logger.info("[Start User Average]")
        self.life = UserAverageLife.objects.create(song_model_size=self.song_model_size)
        pool = ThreadPool(MAX_THREAD)
        user_recommendations_df = pool.map(self.__get_user_average_recommendations, self.user_df['id'].tolist())
        pool.close()
        pool.join()
        logger.info("[Finish User Average]")
        return user_recommendations_df
