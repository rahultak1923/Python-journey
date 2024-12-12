import random

def game():
    print("You are playing the game ")
    score = random.randint(1,62)

    with open("highscore.txt") as f:
        hiscore = f.read()
        if(hiscore!= ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your scrore is {score}")
    if(score>hiscore):
        with open("highscore.txt","w") as f:
            f.write(str(score))
    return score

game()



# with statement to use to read the file 
with open("myfile.txt") as f:
    print(f.read())