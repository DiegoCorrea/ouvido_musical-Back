# O.S. and Python/Django Calls
import logging
# Application Calls
from apps.kemures.similarities.Cosine.cosine_controller import CosineController
from apps.kemures.similarities.Cosine.cosine_overview import CosineOverview
from apps.kemures.kernel_var import SONG_MODEL_SIZE_LIST, TOTAL_RUN

logger = logging.getLogger(__name__)


def one_run_kernel():
    cos = CosineController(1500)
    cos.run_cosine_metadata()


def with_config_run_kernel():
    for song_model_size in SONG_MODEL_SIZE_LIST:
        for i in range(TOTAL_RUN):
            cos = CosineController(song_model_size)
            cos.run_cosine_metadata()
    cos_over = CosineOverview()
    cos_over.make_graphics()
