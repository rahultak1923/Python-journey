# file me se data dekhna 
f = open("file.txt")
data = f.read()
print(data)
f.close()

# file me data add karna
st = "hello i am rahul friend " 
f = open("myfile.txt","w")
f.write(st)
f.close()


# multiple line print in file 
f = open("file.txt")
line = f.readlines()
print(line ,type(line))
f.close()


# file me data add karne ke liye 
f = open("file.txt","a")
st = "hello i am rahul tak "
f.write(st)
f.close()


# file open with the with satement 
with open('myfile.txt')as f:
    print(f.read())