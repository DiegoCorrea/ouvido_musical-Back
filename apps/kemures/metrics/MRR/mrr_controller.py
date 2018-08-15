# -*- coding: utf-8 -*-
# Python and Pip Modules Calls
import logging
import numpy as np
from django.utils import timezone
# Application Calls
from apps.kemures.recommenders.UserAverage.DAO.models import UserAverageLife
from apps.kemures.metrics.MRR.DAO.models import MRR
from apps.kemures.metrics.MRR.runtime.models import MRRRunTime
from apps.kemures.kernel_var import AT_LIST


class MRRController:
    def __init__(self, evaluated_recommendations_df, at_size_list=AT_LIST):
        self.__logger = logging.getLogger(__name__)
        self.__evaluated_recommendations_df = evaluated_recommendations_df
        self.__at_size_list = at_size_list

    @classmethod
    def __get_rr_from_list(cls, relevance_array):
        relevance_list_size = len(relevance_array)
        if relevance_list_size == 0:
            return 0.0
        for i in range(relevance_list_size):
            if relevance_array[i]:
                return 1 / (i + 1)
        return 0.0

    def __calc_users_metric(self, at):
        self.__logger.info("[Calculating Users MRR]")
        users_metric_result_list = []
        for user in self.__evaluated_recommendations_df['user_id'].unique().tolist():
            __user_recommendation_model = self.__evaluated_recommendations_df.loc[
                self.__evaluated_recommendations_df['user_id'] == user]
            __user_recommendation_model.sort_values(by=['similarity'], ascending=False)
            users_metric_result_list.append(MRRController.__get_rr_from_list(__user_recommendation_model['relevance'].tolist()[:at]))
        metric_result = np.mean(users_metric_result_list)
        self.__logger.debug("Mean Reciprocal Rank@%d: %f", at, metric_result)
        self.__logger.debug("Total Users Rated: %d", len(users_metric_result_list))
        return metric_result

    def run_metric(self, at):
        self.__logger.info("[Start Run MRR]")
        started_at = timezone.now()
        value = self.__calc_users_metric(at=at)
        finished_at = timezone.now()
        metric_result_obj = MRR.objects.create(
            round=UserAverageLife.objects.last(),
            value=value,
            at=at
        )
        MRRRunTime.objects.create(
            id=metric_result_obj,
            started_at=started_at,
            finished_at=finished_at
        )
        self.__logger.info(
            "MRR Run Time : "
            + "Start at - "
            + str(started_at)
            + " || Finished at -"
            + str(finished_at)
        )
        self.__logger.info("[Finish Run MRR]")

    def run_for_all_at_size(self):
        for at in self.__at_size_list:
            self.run_metric(at=at)
