import time, random

'''Rock Paper Scissors baby
'''
# Verifies player input is a number is acceptable choice (3, 5 or 7), if not raises error
while True:
    try:
        bestOf = int(input('How many games would you like to play out of? (3, 5 or 7?): '))
        if bestOf not in range(3, 8, 2):
            raise ValueError
    except ValueError:
        print('Oops! Not a valid number. Please try again.')
    playerWins = 0
    computerWins = 0

    while True:

        # Allows computer to randomnly choose value and compares it to the player's choice
        computerOptions = ['r', 's', 'p']
        computerChoice = random.choice(computerOptions)

        playerChoice = input('Please input r, p, or s: ')

        # Iif/elif game logic of choosing rock, paper or scissors
        if playerChoice == 'r' and computerChoice == 's':
            print(f'You chose {playerChoice} and the computer chose {computerChoice}.')
            playerWins += 1
            print(f'Player wins {playerWins} vs. Computer wins {computerWins}')
        elif playerChoice == 'p' and computerChoice == 'r':
            print(f'You chose {playerChoice} and the computer chose {computerChoice}.')
            playerWins += 1
            print(f'Player wins {playerWins} vs. Computer wins {computerWins}')
        elif playerChoice == 's' and computerChoice == 'p':
            print(f'You chose {playerChoice} and the computer chose {computerChoice}.')
            playerWins += 1
            print(f'Player wins {playerWins} vs. Computer wins {computerWins}')
        elif computerChoice == 'r' and playerChoice == 's':
            print(f'You chose {playerChoice} and the computer chose {computerChoice}.')
            computerWins += 1
            print(f'Player wins {playerWins} vs. Computer wins {computerWins}')
        elif computerChoice == 'p' and playerChoice == 'r':
            print(f'You chose {playerChoice} and the computer chose {computerChoice}.')
            computerWins += 1
            print(f'Player wins {playerWins} vs. Computer wins {computerWins}')
        elif computerChoice == 's' and playerChoice == 'p':
            print(f'You chose {playerChoice} and the computer chose {computerChoice}.')
            playerWins += 1
            print(f'Player wins {playerWins} vs. Computer wins {computerWins}')
        elif playerChoice == computerChoice:
            print(f'You chose {playerChoice} and the computer chose {computerChoice}.')
            print('A tie!. Nothing happens')
            print(f'Player wins {playerWins} vs. Computer wins {computerWins}')
            continue

        # Determines is player score is greater than half of the bestOf variable
        if computerWins > bestOf/2:
            print('Aww the computer won. Better luck next time.')
            break
        elif playerWins > bestOf/2:
            print('Nice, you beat that silly computer.')
            break

    break

