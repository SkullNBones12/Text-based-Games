# My version of Mastermind board game

import random, time

# Requires tabulate library install
from tabulate import tabulate

# Random number generator, turns into list to compare index values
secretCode = random.randint(1000, 10000)
# scl is short for Secret Code list, just shorter for all the hint/win conditions
scl = list(map(int, str(secretCode)))

# If loops hits twelve, game exits
loop = 0


print(
    """Hello, welcome to mastermind. You will have to guess a 4 digit code chosen 
by the computer. An 'x' means the number is in the solution but in the 
incorrect position, a '+' means the number is in the correct position and a '/'         
means the number is not a part of the solution."""
)

# Functions that give hints about the solutions. Can't quite figure out how to randomize it.


def hints():
    for index in range(len(uIl)):
        if uIl[index] == scl[index]:
            hintList.append("+")
        elif uIl[index] in scl and uIl[index] != scl[index]:
            hintList.append("x")
        else:
            hintList.append("/")


# Table 2 keeps permanence while Table 1 is empty each new loop
table2 = []
# Hint list is added to each new round
hintList = []

# Main Game Loop
while True:
    # Try/Except loop to verify correct user input
    while True:
        try:
            userInput = int(input())
            if userInput not in range(1000, 10000):
                raise ValueError
            break
        except ValueError:
            print("Please choose an integer between 1000-9999.")
    # uIl stands for User Input List, uIl just shorter for conditionals
    uIl = list(map(int, str(userInput)))

    # Win condition if user input is equal to secret code
    if uIl == scl:
        print("You did it! You guessed my secret code.")
        break

    # Game exits if 12 loops with no correct guess, like board game
    loop += 1

    if loop == 12:
        print("Sorry, better luck next time.")

    # Runs hint functions, creates pretty table with tabulate library, refreshes each loop
    while True:
        hints()
        table1 = [[f"Guess {loop}", (userInput)], [f"Hints: {hintList[-4:]}"]]
        table2.append(table1)
        print(tabulate(table2))
        break
