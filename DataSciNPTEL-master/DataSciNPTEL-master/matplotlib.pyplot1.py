from matplotlib.pylab import *
from pandas import *
data=read_csv("F:/correlation.csv")
scatter(data['x'],data['y'],c='red')
title("Its X vs Y")
xlabel("X")
ylabel("Y")
show()
