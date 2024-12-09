import random

computer = random.choice([1,0,-1])
youstr = input("enter your choice ")
youDict = {"s": 1, "w": -1, "g":0}
you = youDict[youstr]
reversedDict = { 1: "snake", -1 : "water", 0 : "gun" }

print(f"you choose {youstr} \ncomputer choose {reversedDict[computer]}")

if(computer == you ):
    print("Its a draw")
else:
    if(computer ==-1 and you ==1):
        print("you win")

    elif(computer ==-1 and you ==0):
        print("you loss")

    elif(computer ==1 and you ==-1):
        print("you loss")

    elif(computer ==0 and you ==-1):
        print("you win")

    elif(computer ==1 and you ==0):
        print("you win")

    elif(computer ==0 and you ==1):
        print("you loss")

    else:
        print("something went wrong")