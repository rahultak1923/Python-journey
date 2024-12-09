'''

For n = 3
  *
 ***
*****

'''

n = int(input("Enter the number: "))

for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2*i-1))




n=int(input("enter the number "))
for i in range(1, n+1):
    if(i==1 or i==n):
        print("*"*(n-2), end="")
        