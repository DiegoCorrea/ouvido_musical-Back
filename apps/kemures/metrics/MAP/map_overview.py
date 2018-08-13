# -*- coding: utf-8 -*-
import os
import logging

import pandas as pd
import matplotlib.pyplot as plt
from apps.kemures.recommenders.UserAverage.DAO.models import UserAverageLife
from apps.kemures.metrics.MAP.DAO.models import MAP
from apps.kemures.metrics.MAP.runtime.models import MAPRunTime
from apps.kemures.kernel_var import AT_LIST, SONG_MODEL_SIZE_LIST

logger = logging.getLogger(__name__)


class MAPOverview:
    def __init__(self, song_model_size_list=SONG_MODEL_SIZE_LIST, at_size_list=AT_LIST):
        self.directory = str(
            'files/apps/metrics/map/graphs/'
        )
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        self.at_size_list = at_size_list
        self.song_model_size_list = song_model_size_list
        rounds_df = pd.DataFrame.from_records(list(UserAverageLife.objects.all().values()))
        map_df = pd.DataFrame.from_records(list(MAP.objects.all().values()))
        map_run_time_df = pd.DataFrame.from_records(list(MAPRunTime.objects.all().values()))
        self.rounds_collection = pd.DataFrame()
        self.rounds_collection['life'] = rounds_df['id']
        self.rounds_collection['song_model_size'] = rounds_df['song_model_size']
        self.rounds_collection['value'] = map_df['value']
        self.rounds_collection['at'] = map_df['at']
        self.rounds_collection['started_at'] = map_run_time_df['started_at']
        self.rounds_collection['finished_at'] = map_run_time_df['finished_at']

    def make_graphics(self):
        self.all_time_graph_line()
        self.all_time_graph_box_plot()

    def all_time_graph_line(self):
        logger.info("[Start Map Overview - Run Time - (Graph Line)]")
        for size in self.song_model_size_list:
            plt.figure()
            plt.grid(True)
            plt.xlabel('Rodada')
            plt.ylabel('Tempo (segundos)')
            runs_size_df = self.rounds_collection.loc[self.rounds_collection['song_model_size'] == size]
            for at in self.at_size_list:
                runs_size_at_df = runs_size_df.loc[runs_size_df['at'] == at]
                values = [(finished - start).total_seconds() for (finished, start) in zip(runs_size_at_df['finished_at'], runs_size_at_df['started_at'])]
                plt.plot(
                    [i + 1 for i in range(len(values))],
                    [time for time in values],
                    label=at
                )
            plt.legend(loc='best')
            plt.savefig(
                self.directory
                + 'map_metadata_time_graph_line_'
                + str(size)
                + '.png'
            )
            plt.close()
        logger.info("[Finish Map Overview - Run Time - (Graph Line)]")
