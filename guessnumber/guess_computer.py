import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, your guess is too low. Guess again!")
        elif guess > random_number:
            print("Sorry, your guess is too hight. Guess again!")
    print(f"Yay! Congrats! You have guessed the number {random_number} correctly")

guess(10)