# -*- coding: utf-8 -*-
import logging
import os

import matplotlib.pyplot as plt
import pandas as pd

from apps.kemures.kernel.config.global_var import AT_LIST, SONG_SET_SIZE_LIST, MRR_PATH_GRAPHICS
from apps.kemures.kernel.round.models import Round
from apps.kemures.metrics.MRR.DAO.models import MRR
from apps.kemures.metrics.MRR.runtime.models import MRRRunTime


class MRROverview:
    def __init__(self, song_set_size_list=SONG_SET_SIZE_LIST, at_size_list=AT_LIST,
                 directory_to_save_graphics=MRR_PATH_GRAPHICS):
        self.__logger = logging.getLogger(__name__)
        self.__directory_to_save_graphics = str(directory_to_save_graphics)
        if not os.path.exists(self.__directory_to_save_graphics):
            os.makedirs(self.__directory_to_save_graphics)
        self.__at_size_list = at_size_list
        self.__song_set_size_list = song_set_size_list
        rounds_df = pd.DataFrame.from_records(list(Round.objects.all().values()))
        metric_df = pd.DataFrame.from_records(list(MRR.objects.all().values()))
        metric_run_time_df = pd.DataFrame.from_records(list(MRRRunTime.objects.all().values()))
        self.__metric_results_collection_df = pd.DataFrame()
        self.__metric_results_collection_df['song_set_size'] = metric_df['round_id']
        self.__metric_results_collection_df['value'] = metric_df['value']
        self.__metric_results_collection_df['at'] = metric_df['at']
        self.__metric_results_collection_df['started_at'] = metric_run_time_df['started_at']
        self.__metric_results_collection_df['finished_at'] = metric_run_time_df['finished_at']
        for size in self.__song_set_size_list:
            life_size_df = rounds_df.loc[rounds_df['song_set_size'] == size]
            life_id_list = life_size_df['id'].tolist()
            self.__metric_results_collection_df['song_set_size'] = [size if x in life_id_list else x for x in
                                                                    self.__metric_results_collection_df[
                                                                        'song_set_size']]

    def make_time_graphics(self):
        self.__all_time_graph_line()
        self.__all_time_graph_box_plot()

    def __all_time_graph_line(self):
        self.__logger.info("[Start MRR Overview - Run Time - (Graph Line)]")
        for at in self.__at_size_list:
            plt.figure()
            plt.grid(True)
            plt.xlabel('Rodada')
            plt.ylabel('Tempo (segundos)')
            for size in self.__song_set_size_list:
                runs_size_at_df = self.__metric_results_collection_df[
                    (self.__metric_results_collection_df['song_set_size'] == size) & (
                            self.__metric_results_collection_df['at'] == at)]
                values = [(finished - start).total_seconds() for (finished, start) in
                          zip(runs_size_at_df['finished_at'], runs_size_at_df['started_at'])]
                plt.plot(
                    [int(i + 1) for i in range(len(values))],
                    [value for value in values],
                    label=size
                )
            plt.legend(loc='best')
            plt.savefig(
                self.__directory_to_save_graphics
                + 'mrr_all_time_graph_line_'
                + str(at)
                + '.png'
            )
            plt.close()
        self.__logger.info("[Finish MRR Overview - Run Time - (Graph Line)]")

    def __all_time_graph_box_plot(self):
        self.__logger.info("[Start MRR Overview - Run Time - (Graph Box Plot)]")
        for at in self.__at_size_list:
            plt.figure()
            plt.grid(True)
            plt.xlabel('Tamanho do conjunto de músicas')
            plt.ylabel('Tempo (segundos)')
            box_plot_matrix = []
            for size in self.__song_set_size_list:
                runs_size_at_df = self.__metric_results_collection_df[
                    (self.__metric_results_collection_df['song_set_size'] == size) & (
                            self.__metric_results_collection_df['at'] == at)]
                box_plot_matrix.append([(finished - start).total_seconds() for (finished, start) in
                                        zip(runs_size_at_df['finished_at'], runs_size_at_df['started_at'])])
            plt.boxplot(
                box_plot_matrix,
                labels=self.__song_set_size_list
            )
            plt.savefig(
                self.__directory_to_save_graphics
                + 'mrr_all_time_graph_box_plot_'
                + str(at)
                + '.png'
            )
            plt.close()
        self.__logger.info("[Finish MRR Overview - Run Time - (Graph Box Plot)]")

    def make_results_graphics(self):
        self.__all_results_graph_line()
        self.__all_results_graph_box_plot()

    def __all_results_graph_line(self):
        self.__logger.info("[Start MRR Overview - Results - (Graph Line)]")
        for at in self.__at_size_list:
            plt.figure()
            plt.grid(True)
            plt.xlabel('Rodada')
            plt.ylabel('Valor')
            for size in self.__song_set_size_list:
                runs_size_at_df = self.__metric_results_collection_df[
                    (self.__metric_results_collection_df['song_set_size'] == size) & (
                            self.__metric_results_collection_df['at'] == at)]
                values = [value for value in runs_size_at_df['value'].tolist()]
                plt.plot(
                    [int(i + 1) for i in range(len(values))],
                    [value for value in values],
                    label=size
                )
            plt.legend(loc='best')
            plt.savefig(
                self.__directory_to_save_graphics
                + 'mrr_all_results_graph_line_'
                + str(at)
                + '.png'
            )
            plt.close()
        self.__logger.info("[Finish MRR Overview - Results - (Graph Line)]")

    def __all_results_graph_box_plot(self):
        self.__logger.info("[Start MRR Overview - Results - (Graph Box Plot)]")
        for at in self.__at_size_list:
            plt.figure()
            plt.grid(True)
            plt.xlabel('Tamanho do conjunto de músicas')
            plt.ylabel('valor')
            box_plot_matrix = []
            for size in self.__song_set_size_list:
                runs_size_at_df = self.__metric_results_collection_df[
                    (self.__metric_results_collection_df['song_set_size'] == size) & (
                            self.__metric_results_collection_df['at'] == at)]
                box_plot_matrix.append([value for value in runs_size_at_df['value'].tolist()])
            plt.boxplot(
                box_plot_matrix,
                labels=self.__song_set_size_list
            )
            plt.savefig(
                self.__directory_to_save_graphics
                + 'mrr_all_results_graph_box_plot_'
                + str(at)
                + '.png'
            )
            plt.close()
        self.__logger.info("[Finish MRR Overview - Results - (Graph Box Plot)]")
