id=[1,2,3,4]
emp_name=["ram","shyam","preeti","monu"]
num_emp=4
list=[id,emp_name,num_emp]

print(list)
print(list[1][1])
print(list[2])
list[2]=5
print(list[2])
list[1][3]='karan'
print(list)
###############################  appending  #######################################
list[1].append('nirmal')
print(list)
############################## appending another list #############################
list.append([34,45,12,66,12]);print(list)
list[0].insert(4,5);print(list)
############################### deleting list #####################################
del list[3][0];print(list)
############################### remove elemt ######################################
list[1].remove("ram");print(list)
############################### tuple #############################################
t1=(1,2,3,4);t2=(5,6,7,8);t3=t1+t2;
print(t3)
############################### concatinate #######################################














