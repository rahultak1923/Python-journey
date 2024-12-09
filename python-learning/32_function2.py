def goodday(name, god="thank you"):
    print("good morning ",name,god)

goodday("rahul")
goodday("varun","good")


# sum 3 number 
def sum(a,b,c):
    return a+b+c

a = int(input("enter the number "))
b = int(input("enter the number "))
c = int(input("enter the number "))

print("the total sum is ",sum(a,b,c))

# max 3 number

a = int(input("enter the number "))
b = int(input("enter the number "))
c = int(input("enter the number "))

def max(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    elif(c>b and c>a):
        return c
    
print("the max value is ",max(a,b,c))

# function inch to cms 

def inch_to_cms(inch):
    return inch*2.54
print(inch_to_cms(4))