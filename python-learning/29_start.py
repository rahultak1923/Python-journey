'''

For n = 3
  *
 ***
*****

'''

n = int(input("Enter the number: "))

for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2*i-1))




k=int(input("enter the number "))
for i in range(1, k+1):
    if(i==1 or i==k):
        print("*"* k, end="")
    else:
        print("*", end="")
        print(" "* (k-2),end="")
        print("*",end="")
    print("")
        