import matplotlib.pyplot as plt
import pandas
import numpy as np

from api.userPlaySong.models import UserPlaySong
from api.songs.models import SongSimilarity

def playCount():
    plt.figure()
    heard = {'play': [ups.play_count for ups in UserPlaySong.objects.all()]}
    df = pandas.DataFrame(data=heard)
    plt.title('Quantidade de vezes que a música foi ouvida')
    df.boxplot(column='play', meanline=True, showmeans=True)
    plt.savefig('./api/analysis/playCountBoxPlot.png')

def titleSimilarityScatter():
    plt.figure()
    songSimi = [songSimi.similarity for songSimi in SongSimilarity.objects.all()]
    songSimi.sort()
    simiMean = np.mean(songSimi)
    simiMedian = np.median(songSimi)
    plt.title('Similaridade entre as músicas')
    plt.text(-0.1, 1, r'Media: ' + str(simiMean))
    plt.text(-0.1, .8, r'Mediana: ' + str(simiMedian))
    plt.grid(True)
    plt.ylabel('Similaridade')
    plt.xlabel('Similaridade')
    plt.scatter(songSimi, songSimi)
    plt.axis([-0.2, 1.2, -0.2, 1.2])
    plt.savefig('./api/analysis/titleSimilarityScatter.png')
