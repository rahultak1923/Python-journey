#table 
n = int(input("enter the number: "))

for i in range(1,11):
    print(f"{n} X {i} = {n * i}")


# while loop table 
n = int(input("enter the number : "))

i = 1
while(i<=10):
    print(n*i)
    i=i+1


# list name startwith r 

l= ["rahul","rohan","kunal","rinku"]

for name in l:
    if(name.startswith("r")):
        print(f"hello {name}")