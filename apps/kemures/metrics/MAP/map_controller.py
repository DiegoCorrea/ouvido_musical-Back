import logging

import numpy as np
from django.utils import timezone

from apps.kemures.recommenders.UserAverage.DAO.models import UserAverageLife
from apps.kemures.metrics.MAP.DAO.models import MAP
from apps.kemures.metrics.MAP.runtime.models import MAPRunTime

from apps.kemures.kernel_var import AT_LIST

logger = logging.getLogger(__name__)


class MAPController:
    def __init__(self, recommendation_results_df, at_size_list=AT_LIST):
        self.recommendation_results_df = recommendation_results_df
        self.at_size_list = at_size_list

    def __get_ap_from_list(self, relevance_array):
        n_relevances = len(relevance_array)
        if n_relevances == 0:
            return 0.0
        hit_list = []
        relevant = 0
        for i in range(n_relevances):
            if relevance_array[i]:
                relevant += 1
            hit_list.append(relevant / (i + 1))
        ap = sum(hit_list)
        if ap > 0.0:
            return ap / relevant
        else:
            return 0.0

    def __calc_users_map(self, at):
        logger.info("[Start User MAP]")
        ap = []
        for user in self.recommendation_results_df['user_id'].unique().tolist():
            __user_recommendation_model = self.recommendation_results_df.loc[self.recommendation_results_df['user_id'] == user]
            __user_recommendation_model.sort_values(by=['similarity'], ascending=False)
            ap.append(self.__get_ap_from_list(__user_recommendation_model['iLike'].tolist()))
        map_result = np.mean(ap)
        logger.debug("Mean Average Precision@%d: %f", at, map_result)
        logger.debug("Total Users Rated: %d", len(ap))
        logger.info("[Finish User MAP]")
        return map_result

    def run_map(self, at):
        logger.info("[Start Run MAP]")
        started_at = timezone.now()
        value = self.__calc_users_map(at=at)
        finished_at = timezone.now()
        map_result = MAP.objects.create(
            life=UserAverageLife.objects.last(),
            value=value,
            at=at
        )
        MAPRunTime.objects.create(
            id=map_result,
            started_at=started_at,
            finished_at=finished_at
        )
        logger.info(
            "Run Time: Start at - "
            + str(started_at)
            + " || Finished at -"
            + str(finished_at)
        )
        logger.info("[Finish Run MAP]")

    def run_full_map(self):
        for at in self.at_size_list:
            self.run_map(at=at)
