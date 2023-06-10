# Guess the secret number game

import random

x = random.randint(0, 10)
total_guesses = 0

print("Please try and and guess my secret number between 1-10!")

while True:
    while True:
        try:
            guess = int(input())
            break
        except ValueError:
            print("Oops! Not a valid number. Please try again.")

    if guess == x:
        print("Oh, you got me!")
        break
    elif guess > x:
        print("Your number is too high!")
    elif guess < x:
        print("Your number is too low")

    total_guesses += 1
    if total_guesses == 3:
        print("Haha! You lose peasant!")
        break
