import random
import math

# Step 1: Get the range from the user
lower_bound = int(input("Enter the lower bound of the range: "))
upper_bound = int(input("Enter the upper bound of the range: "))

# Step 2: Generate a random number between the given range
random_number = random.randint(lower_bound, upper_bound)

# Step 3: Calculate the minimum number of guesses based on the formula
min_guesses = math.ceil(math.log2(upper_bound - lower_bound + 1))
print(f"\nYou have a maximum of {min_guesses} guesses to find the number.")

# Step 4: Start the guessing game
guesses = 0

while guesses < min_guesses:
    guess = int(input(f"\nGuess a number between {lower_bound} and {upper_bound}: "))
    guesses += 1
    
    if guess < random_number:
        print("Try Again! You guessed too small.")
        lower_bound = guess  # Update the lower bound
    elif guess > random_number:
        print("Try Again! You guessed too high.")
        upper_bound = guess  # Update the upper bound
    else:
        print(f"Congratulations! You guessed the correct number {random_number} in {guesses} guesses!")
        break

# Step 5: If the user fails to guess in the minimum number of guesses
if guesses >= min_guesses and guess != random_number:
    print(f"\nBetter Luck Next Time! The correct number was {random_number}.")
