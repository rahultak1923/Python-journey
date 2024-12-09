# function Definition
def avg():
    a = int(input("enter 1 the number "))
    b = int(input("enter 2 the number "))
    c = int(input("enter 3 the number "))
    avg = (a+b+c)/3
    print(avg)

# function call 
avg()

# function with user input

name = input("enter your name : ")
def people():
    print(f"good morning {name}")

people()

# funciton with arguments 
def goodday(name):
    print("good day ", name)

goodday("varun")

# funciton with arguments and another arguments
def goodday(name, ending):
    print("good day ", name)
    print(ending)

goodday("kunal","thank you")
goodday("maanu","good")

# funciton with arguments and another arguments + return
def goodday(name, ending):
    print("good day ", name)
    print(ending)
    return "ok"

goodday("kunal","thank you")
a= goodday("maanu","good")
print(a)