pos=789
def bin_s(list,n):
    l=0;u=(len(list)-1);
    while l<=u:
        mid = (l + u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1

            else :
                list[mid]>n
                u=mid-1
    return False
list=[45,576,2134,79,4345,67,23,76,12]
list.sort()
print(list)
n=576

if bin_s(list,n):
    print(f"Number {n} found at position ",pos+1)
else:
    print("Not found")