# -*- coding: utf-8 -*-
# Python and Pip Modules Calls
import os
import logging
import pandas as pd
import matplotlib.pyplot as plt
# Application Calls
from apps.kemures.similarities.Cosine.runtime.models import CosineSimilarityRunTime
from apps.kemures.kernel_config.kernel_var import SONG_SET_SIZE_LIST, COSINE_PATH_GRAPHICS


class CosineOverview:
    def __init__(self, song_set_size_list=SONG_SET_SIZE_LIST, directory_to_save_graphics=COSINE_PATH_GRAPHICS,
                 runtime_collection_class=CosineSimilarityRunTime.objects.all().values()):
        self.__logger = logging.getLogger(__name__)
        self.__directory_to_save_graphics = str(directory_to_save_graphics)
        if not os.path.exists(self.__directory_to_save_graphics):
            os.makedirs(self.__directory_to_save_graphics)
        self.__song_set_size_list = song_set_size_list
        self.__runtime_collection_df = pd.DataFrame.from_records(list(runtime_collection_class))

    def make_time_graphics(self):
        self.__all_time_graph_line()
        self.__all_time_graph_box_plot()

    def __all_time_graph_line(self):
        self.__logger.info("[Start Cosine - Run Time - (Graph Line)]")
        plt.figure()
        plt.grid(True)
        plt.xlabel('Rodada')
        plt.ylabel('Tempo (segundos)')
        for size in self.__song_set_size_list:
            runs_size_df = self.__runtime_collection_df.loc[self.__runtime_collection_df['song_set_size'] == size]
            values = [(finished - start).total_seconds() for (finished, start) in
                      zip(runs_size_df['finished_at'], runs_size_df['started_at'])]
            plt.plot(
                [i + 1 for i in range(len(values))],
                [value for value in values],
                label=size
            )
        plt.legend(loc='best')
        plt.savefig(
            self.__directory_to_save_graphics
            + 'cosine_time_graph_line.png'
        )
        plt.close()
        self.__logger.info("[Finish Cosine - Run Time - (Graph Line)]")

    def __all_time_graph_box_plot(self):
        self.__logger.info("[Start Cosine - Run Time - (Graph Box Plot)]")
        plt.figure()
        plt.grid(True)
        plt.xlabel('Tamanho do conjunto de músicas')
        plt.ylabel('Tempo (segundos)')
        box_plot_matrix = []
        for size in self.__song_set_size_list:
            runs_size_df = self.__runtime_collection_df.loc[self.__runtime_collection_df['song_set_size'] == size]
            box_plot_matrix.append([(finished - start).total_seconds() for (finished, start) in
                                    zip(runs_size_df['finished_at'], runs_size_df['started_at'])])
        plt.boxplot(
            box_plot_matrix,
            labels=self.__song_set_size_list
        )
        plt.savefig(
            self.__directory_to_save_graphics
            + 'cosine_time_graph_box_plot.png'
        )
        plt.close()
        self.__logger.info("[Finish Cosine - Run Time - (Graph BoxPlot)]")
