# O.S. and Python/Django Calls
import os
import logging
# Modules Calls
import pandas as pd
import matplotlib.pyplot as plt
# Application Calls
from apps.kemures.recommenders.UserAverage.runtime.models import UserAverageRunTime
from apps.kemures.kernel_var import SONG_MODEL_SIZE_LIST

logger = logging.getLogger(__name__)


class UserAverageOverview:
    def __init__(self, song_model_size_list=SONG_MODEL_SIZE_LIST):
        self.directory = str(
            'files/apps/recommenders/UserAverage/graphs/'
        )
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        self.song_model_size_list = song_model_size_list
        self.runtime_collection = pd.DataFrame.from_records(list(UserAverageRunTime.objects.all().values()))

    def make_graphics(self):
        self.all_time_graph_line()
        self.all_time_graph_box_plot()

    def all_time_graph_line(self):
        logger.info("[Start User Average - Run Time - (Graph Line)]")
        plt.figure()
        plt.grid(True)
        plt.xlabel('Rodada')
        plt.ylabel('Tempo (segundos)')
        for size in self.song_model_size_list:
            runs = self.runtime_collection.loc[self.runtime_collection['song_model_size'] == size]
            values = [(finished - start).total_seconds() for (finished, start) in zip(runs['finished_at'], runs['started_at'])]
            plt.plot(
                [i + 1 for i in range(len(values))],
                [time for time in values],
                label=size
            )
        plt.legend(loc='best')
        plt.savefig(
            self.directory
            + 'user_average_time_graph_line.png'
        )
        plt.close()
        logger.info("[Finish User Average - Run Time - (Graph Line)]")

    def all_time_graph_box_plot(self):
        logger.info("[Start User Average - Run Time - (Graph BoxPlot)]")
        plt.figure()
        plt.grid(True)
        plt.xlabel('Tamanho do modelos das músicas')
        plt.ylabel('Tempo (segundos)')
        box_plot_matrix = []
        for size in self.song_model_size_list:
            runs = self.runtime_collection.loc[self.runtime_collection['song_model_size'] == size]
            box_plot_matrix.append([(finished - start).total_seconds() for (finished, start) in zip(runs['finished_at'], runs['started_at'])])
        plt.boxplot(
            box_plot_matrix,
            labels=self.song_model_size_list
        )
        plt.savefig(
            self.directory
            + 'user_average_time_graph_box_plot.png'
        )
        plt.close()
        logger.info("[Finish User Average - Run Time - (Graph BoxPlot)]")