# -*- coding: utf-8 -*-
import logging
import os

import matplotlib.pyplot as plt
import pandas as pd

from apps.kemures.kernel.config.global_var import METADATA_OPTION_GRAPH, NDCG_PATH_GRAPHICS
from apps.kemures.kernel.round.models import Round
from apps.kemures.metrics.NDCG.DAO.models import NDCG
from apps.kemures.metrics.NDCG.runtime.models import NDCGRunTime


class NDCGOverview:
    def __init__(self, directory_to_save_graphics=NDCG_PATH_GRAPHICS):
        self.__logger = logging.getLogger(__name__)
        self.__directory_to_save_graphics = str(directory_to_save_graphics)
        if not os.path.exists(self.__directory_to_save_graphics):
            os.makedirs(self.__directory_to_save_graphics)
        rounds_df = pd.DataFrame.from_records(list(Round.objects.all().values()))
        rounds_df = rounds_df.drop(columns=['finished_at', 'started_at'])
        metric_df = pd.DataFrame.from_records(list(NDCG.objects.all().values()))
        metric_run_time_df = pd.DataFrame.from_records(list(NDCGRunTime.objects.all().values()))
        self.__metadata_to_process = rounds_df['metadata_used'].unique().tolist()
        self.__song_set_size_list = rounds_df['song_set_size'].unique().tolist().sort()
        self.__user_set_size_list = rounds_df['user_set_size'].unique().tolist().sort()
        self.__at_size_list = metric_df['at'].unique().tolist().sort()
        self.__graph_style = METADATA_OPTION_GRAPH[:len(self.__metadata_to_process)]
        self.__metric_results_collection_df = metric_df.copy()
        self.__metric_results_collection_df = self.__metric_results_collection_df.join(
            metric_run_time_df.set_index('id_id'), on='id')
        self.__metric_results_collection_df = self.__metric_results_collection_df.join(rounds_df.set_index('id'),
                                                                                       on='round_id')

    def make_time_graphics(self):
        self.__all_time_graph_line()
        self.__all_time_graph_box_plot()

    def __all_time_graph_line(self):
        self.__logger.info("[Start NDCG Overview - Run Time - (Graph Line)]")
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
                + 'ndcg_all_time_graph_line_'
                + str(at)
                + '.png'
            )
            plt.close()
        self.__logger.info("[Finish NDCG Overview - Run Time - (Graph Line)]")

    def __all_time_graph_box_plot(self):
        self.__logger.info("[Start NDCG Overview - Run Time - (Graph Box Plot)]")
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
                + 'ndcg_all_time_graph_box_plot_'
                + str(at)
                + '.png'
            )
            plt.close()
        self.__logger.info("[Finish NDCG Overview - Run Time - (Graph Box Plot)]")

    def make_results_graphics(self):
        self.__by_length_results_graph_line()
        self.__by_length_results_graph_box_plot()

    def __by_length_results_graph_line(self):
        self.__logger.info("[Start NDCG Overview - Results - (Graph Line)]")
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
                + 'ndcg_all_results_graph_line_'
                + str(at)
                + '.png'
            )
            plt.close()
        self.__logger.info("[Finish NDCG Overview - Results - (Graph Line)]")

    def __by_length_results_graph_box_plot(self):
        self.__logger.info("[Start NDCG Overview - Results - (Graph Box Plot)]")
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
                + 'ndcg_all_results_graph_box_plot_'
                + str(at)
                + '.png'
            )
            plt.close()
        self.__logger.info("[Finish NDCG Overview - Results - (Graph Box Plot)]")

    def make_graphics_by_metadata(self):
        self.__by_metadata_results_graph_line()
        self.__by_metadata_results_graph_box_plot()
        self.__save_csv()

    def __by_metadata_results_graph_line(self):
        self.__logger.info("[Start NDCG Overview - Results - (Graph Line)]")
        plt.figure()
        plt.grid(True)
        plt.xlabel('Tamanho da lista de recomendação')
        plt.ylabel('Valor')
        for metadata, style in zip(self.__metadata_to_process, self.__graph_style):
            at_df = self.__metric_results_collection_df[
                self.__metric_results_collection_df['metadata_used'] == metadata]
            at_df.sort_values("at")
            plt.plot(
                at_df['at'],
                at_df['value'],
                style,
                label=metadata
            )
        plt.legend(loc='best')
        plt.xticks(self.__at_size_list)
        plt.savefig(
            self.__directory_to_save_graphics
            + 'ndcg_by_metadata_results_graph_line_'
            + '.png'
        )
        plt.close()
        self.__logger.info("[Finish NDCG Overview - Results - (Graph Line)]")

    def __by_metadata_results_graph_box_plot(self):
        self.__logger.info("[Start NDCG Overview - Results - (Graph Box Plot)]")
        plt.figure()
        plt.grid(True)
        plt.xlabel('Metadado')
        plt.ylabel('valor')
        box_plot_matrix = []
        for metadata in self.__metadata_to_process:
            at_df = self.__metric_results_collection_df[
                self.__metric_results_collection_df['metadata_used'] == metadata]
            box_plot_matrix.append([value for value in at_df['value'].tolist()])
        plt.boxplot(
            box_plot_matrix,
            labels=self.__metadata_to_process
        )
        plt.savefig(
            self.__directory_to_save_graphics
            + 'ndcg_by_metadata_results_graph_box_plot_'
            + '.png'
        )
        plt.close()
        self.__logger.info("[Finish NDCG Overview - Results - (Graph Box Plot)]")

    def __save_csv(self):
        self.__metric_results_collection_df.to_csv(self.__directory_to_save_graphics + 'MAP.csv')
