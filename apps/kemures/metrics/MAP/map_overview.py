# -*- coding: utf-8 -*-
# Python and Pip Modules Calls
import os
import logging
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Application Calls
from apps.kemures.recommenders.UserAverage.DAO.models import UserAverageLife
from apps.kemures.metrics.MAP.DAO.models import MAP
from apps.kemures.metrics.MAP.runtime.models import MAPRunTime
from apps.kemures.kernel_var import AT_LIST, SONG_MODEL_SIZE_LIST


class MAPOverview:
    def __init__(self, song_model_size_list=SONG_MODEL_SIZE_LIST, at_size_list=AT_LIST):
        self.__logger = logging.getLogger(__name__)
        self.__directory = str(
            'files/apps/metrics/map/graphs/'
        )
        if not os.path.exists(self.__directory):
            os.makedirs(self.__directory)
        self.__at_size_list = at_size_list
        self.__song_model_size_list = song_model_size_list
        rounds_df = pd.DataFrame.from_records(list(UserAverageLife.objects.all().values()))
        map_df = pd.DataFrame.from_records(list(MAP.objects.all().values()))
        map_run_time_df = pd.DataFrame.from_records(list(MAPRunTime.objects.all().values()))
        self.__rounds_collection = pd.DataFrame()
        self.__rounds_collection['song_model_size'] = map_df['life_id']
        self.__rounds_collection['value'] = map_df['value']
        self.__rounds_collection['at'] = map_df['at']
        self.__rounds_collection['started_at'] = map_run_time_df['started_at']
        self.__rounds_collection['finished_at'] = map_run_time_df['finished_at']
        for size in self.__song_model_size_list:
            life_size_df = rounds_df.loc[rounds_df['song_model_size'] == size]
            life_id_list = life_size_df['id'].tolist()
            self.__rounds_collection['song_model_size'] = [size if x in life_id_list else x for x in
                                                           self.__rounds_collection['song_model_size']]

    def make_time_graphics(self):
        self.__all_time_graph_line()
        self.__all_time_graph_box_plot()

    def __all_time_graph_line(self):
        self.__logger.info("[Start Map Overview - Run Time - (Graph Line)]")
        for at in self.__at_size_list:
            plt.figure()
            plt.grid(True)
            plt.xlabel('Rodada')
            plt.ylabel('Tempo (segundos)')
            for size in self.__song_model_size_list:
                runs_size_at_df = self.__rounds_collection[
                    (self.__rounds_collection['song_model_size'] == size) & (self.__rounds_collection['at'] == at)]
                values = [(finished - start).total_seconds() for (finished, start) in
                          zip(runs_size_at_df['finished_at'], runs_size_at_df['started_at'])]
                plt.plot(
                    [int(i + 1) for i in range(len(values))],
                    [value for value in values],
                    label=size
                )
            plt.legend(loc='best')
            plt.savefig(
                self.__directory
                + 'map_all_time_graph_line_'
                + str(at)
                + '.png'
            )
            plt.close()
        self.__logger.info("[Finish Map Overview - Run Time - (Graph Line)]")

    def __all_time_graph_box_plot(self):
        self.__logger.info("[Start Map Overview - Run Time - (Graph Box Plot)]")
        for at in self.__at_size_list:
            plt.figure()
            plt.grid(True)
            plt.xlabel('Tamanho do modelos das músicas')
            plt.ylabel('Tempo (segundos)')
            box_plot_matrix = []
            for size in self.__song_model_size_list:
                runs_size_at_df = self.__rounds_collection[
                    (self.__rounds_collection['song_model_size'] == size) & (self.__rounds_collection['at'] == at)]
                box_plot_matrix.append([(finished - start).total_seconds() for (finished, start) in
                                        zip(runs_size_at_df['finished_at'], runs_size_at_df['started_at'])])
            plt.boxplot(
                box_plot_matrix,
                labels=self.__song_model_size_list
            )
            plt.savefig(
                self.__directory
                + 'map_all_time_graph_box_plot_'
                + str(at)
                + '.png'
            )
            plt.close()
        self.__logger.info("[Finish Map Overview - Run Time - (Graph Box Plot)]")

    def make_results_graphics(self):
        self.__all_results_graph_line()
        self.__all_results_graph_box_plot()

    def __all_results_graph_line(self):
        self.__logger.info("[Start Map Overview - Results - (Graph Line)]")
        for at in self.__at_size_list:
            plt.figure()
            plt.grid(True)
            plt.xlabel('Rodada')
            plt.ylabel('Valor')
            for size in self.__song_model_size_list:
                runs_size_at_df = self.__rounds_collection[
                    (self.__rounds_collection['song_model_size'] == size) & (self.__rounds_collection['at'] == at)]
                values = [value for value in runs_size_at_df['value'].tolist()]
                plt.plot(
                    [int(i + 1) for i in range(len(values))],
                    [value for value in values],
                    label=size
                )
            plt.legend(loc='best')
            plt.savefig(
                self.__directory
                + 'map_all_results_graph_line_'
                + str(at)
                + '.png'
            )
            plt.close()
        self.__logger.info("[Finish Map Overview - Results - (Graph Line)]")

    def __all_results_graph_box_plot(self):
        self.__logger.info("[Start Map Overview - Results - (Graph Box Plot)]")
        for at in self.__at_size_list:
            plt.figure()
            plt.grid(True)
            plt.xlabel('Tamanho do modelos das músicas')
            plt.ylabel('valor')
            box_plot_matrix = []
            for size in self.__song_model_size_list:
                runs_size_at_df = self.__rounds_collection[
                    (self.__rounds_collection['song_model_size'] == size) & (self.__rounds_collection['at'] == at)]
                box_plot_matrix.append([value for value in runs_size_at_df['value'].tolist()])
            plt.boxplot(
                box_plot_matrix,
                labels=self.__song_model_size_list
            )
            plt.savefig(
                self.__directory
                + 'map_all_results_graph_box_plot_'
                + str(at)
                + '.png'
            )
            plt.close()
        self.__logger.info("[Finish Map Overview - Results - (Graph Box Plot)]")
