import matplotlib.pyplot as plt
import pandas
import numpy as np

from api.userPlaySong.models import UserPlaySong

def playCountData():
    playList = [ ups.play_count for ups in UserPlaySong.objects.all()]
    playMean = np.mean(playList)
    playMedian = np.median(playList)
    return {'mean': playMean, 'median': playMedian}
