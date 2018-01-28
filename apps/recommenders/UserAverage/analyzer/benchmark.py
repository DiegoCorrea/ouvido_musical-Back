import matplotlib.pyplot as plt
import numpy as np
import logging
import os

from collections import Counter
from apps.recommenders.UserAverage.algorithm.models import (
    UserAverage_Recommendations,
    UserAverage_Life
)
from apps.recommenders.UserAverage.benchmark.models import BenchUserAverage

logger = logging.getLogger(__name__)
