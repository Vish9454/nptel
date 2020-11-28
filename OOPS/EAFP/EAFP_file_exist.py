file="EAFP.py"
try:
    f=open(file)
except IOError as e:
    print("File cannot be accesed")
else:
    with f:
        print(f.read())