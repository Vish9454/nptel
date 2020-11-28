import seaborn as sns
import matplotlib.pylab as mp
import pandas as pan
from numpy import *

data=pan.read_csv("F:/nba.csv")
#data=pan.read_csv("F:/correlation.csv")
data.dropna(axis=0,inplace=True)
'''
data.dropna(axis=0,inplace=True)
data['X']=data['X'].astype(int)
data['Y']=data['Y'].astype(int)
print(data.info())
sns.set(style="darkgrid")
#sns.regplot(x=data['X'],y=data['Y'],marker='*')
sns.lmplot(x='X',y='Y',data=data,hue='obj',legend=True,palette="Set1")
mp.show()
'''
#distplot(data['X'],kde=False,bins=5)
#show()

#countplot(x='Position',data=data,hue='Team')
#show()

#sns.boxplot(x=data["Position"],y=data["Salary"],hue=data["Team"])
#mp.show()

#sns.distplot(data["Salary"],ax=ax_hist ,kde=False)
#sns.boxplot(data["Position"],ax=ax_box)
#f,(ax_box, ax_box)=mp.subplot(2,gridspec_kw={"height_ratios": (.15,.85)})
sns.pairplot(data,kind="scatter",hue="Position")
mp.show()