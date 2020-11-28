from matplotlib.pylab import plt
from pandas import *
data=read_csv("F:/correlation.csv")
plt.hist(data['X'],color='green')
plt.title("Histogram")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()

