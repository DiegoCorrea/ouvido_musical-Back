from .algorithm.caller import main
from apps.kemures.CONSTANTS import SET_SIZE_LIST, TOTAL_RUN

import pandas as pd
import logging
logger = logging.getLogger(__name__)


class Cosine:
    def __init__(self):
        self.metadata_df = pd.DataFrame(columns=list([]))

    def run_cosine(self):
        logger.info("[Start Title Similarity with Cosine]")
        main(self.metadata_df)
        logger.info("[Finish Title Similarity with Cosine]")

    def run_with_config(self, set_size):
        logger.info("[Start Similarities]")
        for setSize in SET_SIZE_LIST:
            for run in range(TOTAL_RUN):
                main()
        logger.info("[Finish Similarities]")
