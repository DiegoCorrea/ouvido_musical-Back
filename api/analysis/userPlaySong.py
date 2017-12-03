import matplotlib.pyplot as plt
import pandas

from api.userPlaySong.models import UserPlaySong

def heardBoxPlot():
    plt.figure()
    heard = { 'play': [ ups.play_count for ups in UserPlaySong.objects.all()]}
    df = pandas.DataFrame(data=heard)
    df.boxplot(column='play')
    plt.savefig('heardBoxPlot.png')
