def ArrayChallenge(arr):
  l1=[];l2=[];count=0
  # code goes here
  for i in range(arr[0],arr[1]):
    l1.append(i)
  l1.append(i+1)
  print(l1)
  for j in range(arr[2],arr[3]):
    l2.append(j)
  l2.append(j+1)
  print(l2)
  p=(set(l1)&set(l2))
  print(len(p))

  x=arr[4]
  if x==p:
    return True
  else:
    return False

# keep this function call here
print(ArrayChallenge([1,8,2,4,4]))