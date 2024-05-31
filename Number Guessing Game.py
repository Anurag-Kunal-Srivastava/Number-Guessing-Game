import random

# Generate a random number between 1 and 10 (inclusive)
number = random.randrange(1, 11)

guess = int(input("Enter guess number between 1 - 10:- "))

attempts  = 1 # Track Number of guesses

while guess != number:
    if guess < number:
        print("Too Low, Try Again")
    else:
        print("Too High, Try Again")
    guess = int(input("Enter guess number between 1 - 10:- "))
    attempts += 1

print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
