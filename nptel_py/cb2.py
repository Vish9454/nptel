def ArrayChallenge(arr):
  freq={};l=[]
  for items in arr:
    if items in freq:
      freq[items]+=1
    else:
      freq[items]=1
  for x,y in freq.items():
    l.append(y)
  # code goes here
  if max(l)==1:
    return 0
  else:
    return max(l)
# keep this function call here
print(ArrayChallenge([0,-2,-2,-2,-2,5,5,5]))