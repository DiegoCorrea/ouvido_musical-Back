import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from apps.evaluators.MAP.algorithm.models import MAP
def MAP_value_gLine(limit=5):
    allMAP = MAP.objects.all()
    mapValues = [result.value for result in allMAP]
    mapMean = np.mean(mapValues)
    mapMedian = np.median(mapValues)
    plt.figure()
    plt.text(-0.1, 1, r'Media: ' + str(mapMean))
    plt.text(-0.1, .8, r'Mediana: ' + str(mapMedian))
    plt.grid(True)
    plt.xlabel('Tempo de execução')
    plt.ylabel('Valor do MAP')
    plt.title('MAP - Mean Averange Precision')
    plt.plot([result.id for result in allMAP],[result.value for result in allMAP])
    plt.savefig('./apps/evaluators/MAP/analyze/MAP_value_gLine.png')
