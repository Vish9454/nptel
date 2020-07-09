import os
print(os.stat("/home/django_resume/nptel_py/rough.py"))


print("WQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")
import os
list = os.listdir("/home/django_resume") # dir is your directory path
number_files = len(list)
print(list) # displays all the files and folders in the directory
print(number_files) # displays no of files and folders in the directory

#Only files (avoiding subdirectories) in that particular directory
#os.walk retrns 3 values i.e
# [0] as root dir , [1] as directory in that folder ,[2] as files in that directory
onlyfiles = next(os.walk("/home/django_resume"))[2]
print(onlyfiles)

print("#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
import os
for root,dirs,files in os.walk("/home/django_resume"):
    for filename in files:
        print(filename)
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
import sys
print(sys.argv)
import os
f=open("rough.py","r")
text=f.read()
print(text)