from matplotlib.pylab import *

fueltype=['Petrol','Diesel','CNG']
xlen=arange(len(fueltype))

y=[16,13,44]

bar(xlen,y,color=['red','green','cyan'])
title=("Its bar plot")
xlabel=("Fuel type")
ylabel=("Numbers")
xticks(xlen,fueltype,rotation=90)
show()


