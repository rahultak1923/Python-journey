# factorial number in recursion function 
def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)

n = int(input("enter the factorial number "))
print(f"the factoral value is {factorial(n)}")


# first 10 nactural number 

def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n
print(sum(4))


# start paten in recursion function 
def star(n):
    if(n==0):
        return
    print("*"*n)
    star(n-1)
star(5)