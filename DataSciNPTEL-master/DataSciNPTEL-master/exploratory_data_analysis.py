from pandas import *

data=read_csv("F:/nba.csv",index_col=0)
print(data)
datacopy=data.copy()
print("Category of team wise frequency")
print(crosstab(index=datacopy['Team'],columns='count',dropna=True))

print("group by of Team and Position and Position is index","Headers will be Team and positions will be index")
print(crosstab(index=datacopy["Position"],columns=datacopy["Team"],dropna=True))

print("joint probability of having position of players in a certain team is as ")
print("Atlanta kay center(C) position pe khaelnay wala bando ki probaility 0.0065 hai aur PF position pe .0087 hai")
print("Is team kay Is position pe bando ki khalney ki probability ye hai")
print(crosstab(index=datacopy["Position"],columns=datacopy["Team"],normalize=True,dropna=True))

print("marginal probalility gives probability of the outcomes")
print(crosstab(index=datacopy["Position"],columns=datacopy["Team"],normalize=True,dropna=True,margins=True))

print("Conditional probability is sum of rows probability is 1")
print(crosstab(index=datacopy["Position"],columns=datacopy["Team"],dropna=True,normalize='index',margins=True))

print(crosstab(index=datacopy["Position"],columns=datacopy["Team"],margins=True,dropna=True,normalize='columns'))

print()