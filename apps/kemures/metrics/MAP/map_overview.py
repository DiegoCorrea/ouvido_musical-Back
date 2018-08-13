# -*- coding: utf-8 -*-
import os

import pandas as pd

from apps.kemures.metrics.MAP.DAO.models import MAP
from apps.kemures.metrics.MAP.runtime.models import MAPRunTime


class MapOverview:
    def __init__(self, evaluated_recommendations_df, at_size_list=AT_LIST):
        self.directory = str(
            'files/apps/metrics/map/graphs/'
        )
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        self.evaluated_recommendations_df = evaluated_recommendations_df
        self.at_size_list = at_size_list
        self.runtime_collection = pd.DataFrame.from_records(list(MapRunTime.objects.all().values()))

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
            runs_size_df = self.runtime_collection.loc[self.runtime_collection['song_model_size'] == size]
            for at in self.at_size_list:
                runs = self.runs_size_df.loc[self.runs_size_df['at'] == at]
                values = [(finished - start).total_seconds() for (finished, start) in zip(runs['finished_at'], runs['started_at'])]
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

    def all_time_graph_box_plot(self):
        logger.info("[Start Cosine - Run Time - (Graph BoxPlot)]")
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
            + 'cosine_metadata_time_graph_box_plot.png'
        )
        plt.close()
        logger.info("[Finish Cosine - Run Time - (Graph BoxPlot)]")

