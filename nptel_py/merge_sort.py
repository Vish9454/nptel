def merge(A, B):
    (C, m, n) = ([], len(A), len(B))
    (i, j) = (0, 0)
    while (i + j) < (m + n):
        if i == m:
            C.append(B[j])
            j = j + 1
        elif j == n:
            C.append(A[i])
            i = i + 1
        elif A[i] <= B[j]:
            C.append(A[i])
            i = i + 1
        elif A[i] > B[j]:
            C.append(B[j])
            j = j + 1
    return C


def mergesort(A, left, right):  # A[left:right]
    if right - left <= 1:
        return A[left:right]
    if right - left > 1:
        mid = (left + right) // 2
        L = mergesort(A, left, mid);print("L",L)
        R = mergesort(A, mid, right);print("R",R)
        return merge(L, R)


a = list(range(7, 1, -2)) + list(range(6, 1, -2))
print("a =",a)
print(mergesort(a, 0, len(a)))
