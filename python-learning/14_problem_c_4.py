number = []

f1 = int(input("Enter the number: "))  # Convert input to integer
number.append(f1)

f2 = int(input("Enter the number: "))
number.append(f2)

f3 = int(input("Enter the number: "))
number.append(f3)

f4 = int(input("Enter the number: "))
number.append(f4)

f5 = int(input("Enter the number: "))
number.append(f5)

number.sort()  # Now the list contains integers, so sorting works as expected
print(number)




# sum 4 number in python by tuple 

num = (123,27,50,100)
print(sum(num))

# cout number in tuple 

a = (1,2,1,2,1,1,5,1)
print(a.count(1))