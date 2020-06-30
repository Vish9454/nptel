def InsertionSort(seq):
    isort(seq, len(seq))

def isort(seq, k):
    if k > 1:
        print(seq, " ", k)
        isort(seq, k - 1)
        insert(seq, k - 1)
        print("<<isort print",k,seq,">>")

def insert(seq, k):
    pos = k
    while pos > 0 and seq[pos] < seq[pos - 1]:
        (seq[pos], seq[pos - 1]) = (seq[pos - 1], seq[pos])
        pos = pos - 1
    print(k,seq,end=" ")

l=list(range(4,0,-1))
InsertionSort(l)



