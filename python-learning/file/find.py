with open("myfile.txt") as f:
    contant = f.read()
if("rahul" in contant):
    print("yes rahul is present")
else:
    print("rahul is not present")