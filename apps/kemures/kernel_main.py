# O.S. and Python/Django Calls
import os
import logging
from apps.kemures.similarities.Cosine.cosine_controller import Cosine

logger = logging.getLogger(__name__)


def one_run_kernel():
    cos = Cosine()
    cos.run_cosine_metadata()
