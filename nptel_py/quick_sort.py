def Quicksort(A,l,r):    #  A[l:r]
    if r-l<=1:
        return ()
    yellow=l+1    # At l position now is the pivot element so yellow is the l+1 position
    for green in range(l+1,r):
        if A[green]<=A[l]:
            A[yellow],A[green]=A[green],A[yellow]
            yellow=yellow+1
    A[l],A[yellow-1]=A[yellow-1],A[l]
    print(A)
    Quicksort(A,l,yellow-1)
    Quicksort(A,yellow,r)

l=[43,32,22,13,63,57,91,78]
Quicksort(l,0,len(l))
print(l)

