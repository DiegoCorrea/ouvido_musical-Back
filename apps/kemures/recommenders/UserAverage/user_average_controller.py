# -*- coding: utf-8 -*-
# O.S. and Python/Django Calls
from django.utils import timezone
import logging
# Modules Calls

# Application Calls
from apps.kemures.recommenders.UserAverage.DAO.models import UserAverage_Recommendations, UserAverage_Life
from apps.kemures.recommenders.UserAverage.runtime.models import UserAverageRunTime

logger = logging.getLogger(__name__)


class UserAverageController:
    def __init__(self, similarity_matrix):
        self.similarity_matrix = similarity_matrix

    def run_user_average(self):
        logger.info("[Start Run User Average - Benchmark]")
        started_at = timezone.now()
        self.UserAverage(songSetLimit=songSetLimit)
        finished_at = timezone.now()
        UserAverageRunTime.objects.create(
            life=UserAverage_Life.objects.last(),
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