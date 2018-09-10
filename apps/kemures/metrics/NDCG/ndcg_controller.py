# -*- coding: utf-8 -*-
import logging

import numpy as np
from django.utils import timezone

from apps.kemures.kernel.config.global_var import AT_LIST
from apps.kemures.metrics.NDCG.DAO.models import NDCG
from apps.kemures.metrics.NDCG.runtime.models import NDCGRunTime


class NDCGController:
    def __init__(self, evaluated_recommendations_df, round_instance, at_size_list=AT_LIST):
        self.__logger = logging.getLogger(__name__)
        self.__evaluated_recommendations_df = evaluated_recommendations_df
        self.__at_size_list = at_size_list
        self.__round_instance = round_instance

    @classmethod
    def __dcg_at_k(cls, r, k, method=0):
        r = np.asfarray(r)[:k]
        if r.size:
            if method == 0:
                return r[0] + np.sum(r[1:] / np.log2(np.arange(2, r.size + 1)))
            elif method == 1:
                return np.sum(r / np.log2(np.arange(2, r.size + 2)))
            else:
                raise ValueError('method must be 0 or 1.')
        return 0.

    @classmethod
    def __ndcg_at_k(cls, r, k, method=0):
        score = [float(i) for i in r]
        dcg_max = NDCGController.__dcg_at_k(sorted(score, reverse=True), k, method)
        if not dcg_max:
            return 0.
        return NDCGController.__dcg_at_k(r, k, method) / dcg_max

    def __calc_users_metric(self, at):
        self.__logger.info("[Calculating Users NDCG]")
        users_metric_result_list = []
        for user in self.__evaluated_recommendations_df['user_id'].unique().tolist():
            __user_recommendation_model = self.__evaluated_recommendations_df.loc[
                self.__evaluated_recommendations_df['user_id'] == user]
            __user_recommendation_model.sort_values(by=['similarity'], ascending=False)
            users_metric_result_list.append(self.__ndcg_at_k(
                __user_recommendation_model['global_relevance_score'].tolist()[:at],
                k=at,
                method=0

            ))
        metric_result = np.mean(users_metric_result_list)
        self.__logger.debug("Normalized Cumulative Gain@%d: %f", at, metric_result)
        self.__logger.debug("Total Users Rated: %d", len(users_metric_result_list))
        return metric_result

    def run_metric(self, at):
        self.__logger.info("[Start Run NDCG]")
        started_at = timezone.now()
        value = self.__calc_users_metric(at=at)
        finished_at = timezone.now()
        metric_result_obj = NDCG.objects.create(
            round=self.__round_instance,
            value=value,
            at=at
        )
        NDCGRunTime.objects.create(
            id=metric_result_obj,
            started_at=started_at,
            finished_at=finished_at
        )
        self.__logger.info(
            "NDCG Run Time : "
            + "Start at - "
            + str(started_at)
            + " || Finished at -"
            + str(finished_at)
        )
        self.__logger.info("[Finish Run NDCG]")

    def run_for_all_at_size(self):
        for at in self.__at_size_list:
            self.run_metric(at=at)
