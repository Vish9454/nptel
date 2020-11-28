from numpy import *
mat1=matrix("1,2,3;4,5,6;7,8,9");print(mat1)
mat2=matrix("1,2;3,4");print(mat2)
print(int(linalg.det(mat1)))
print(int(linalg.det(mat2)))
print(linalg.matrix_rank(mat1))
print(linalg.matrix_rank(mat2))
1
