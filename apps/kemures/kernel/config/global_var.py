# Kernel Threads
MAX_THREAD = 3

USER_SIZE = 1000
USER_SIZE_LIST = [100, 500, 1000]
SONG_SIZE = 10000
SONG_SET_SIZE_LIST = [3000, 6000, 10000]

METADATA_TO_PROCESS_LIST_PT = ['Título', 'Artista', 'Álbum']
METADATA_TO_PROCESS_LIST_EN = ['Title', 'Artist', 'Album']
METADATA_TO_PROCESS_LIST = ['title', 'artist', 'album']
METADATA_OPTION_GRAPH = ['o', '^', 's', 'D', 'x', 'p', '.', '1', '|', '*', '2']
GRAPH_MARKERS = ['o', '^', 's', 'D', 'x', 'p', '.', '1', '|', '*', '2']
GRAPH_STYLE = [':', ':', ':', '-', '-', '-', '--', '--', '--', '-.', '-.']
GRAPH_COLORS = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray',
                'tab:olive', 'tab:cyan', '#0F0F0F0F']

RECOMMENDATION_LIST_SIZE = 20
TOTAL_RUN = 10

AT_LIST = [1, 5, 10, 15, 20]

# List of paths to save Graphics and CSV
COSINE_PATH_GRAPHICS = 'files/kemures/similarities/cosine/'
USER_AVERAGE_PATH_GRAPHICS = 'files/kemures/recommenders/userAverage/'
MAP_PATH_GRAPHICS = 'files/kemures/metrics/map/'
MRR_PATH_GRAPHICS = 'files/kemures/metrics/mrr/'
NDCG_PATH_GRAPHICS = 'files/kemures/metrics/ndcg/'
