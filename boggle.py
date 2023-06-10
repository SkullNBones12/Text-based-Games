# Boggle board
import random, time, sys

countdown = 180

b = ['']*16

def prettyBoard():
    '''Makes b into the pretty board''' 
    print(f'{(b[0])} {(b[1])} {(b[2])} {(b[3])}')
    print(f'{(b[4])} {(b[5])} {(b[6])} {(b[7])}')
    print(f'{(b[8])} {(b[9])} {(b[10])} {(b[11])}')
    print(f'{(b[12])} {(b[13])} {(b[14])} {(b[15])}')


dicePool = [
    ['R', 'I', 'F', 'O', 'B', 'X'],
    ['I', 'F', 'E', 'H', 'E', 'Y'],
    ['D', 'E', 'N', 'O', 'W', 'S'],
    ['U', 'T', 'O', 'K', 'N', 'D'],
    ['H', 'M', 'S', 'R', 'A', 'O'],
    ['L', 'U', 'P', 'E', 'T', 'S'],
    ['A', 'C', 'I', 'T', 'O', 'A'],
    ['Y', 'L', 'G', 'K', 'U', 'E'],
    ['Qu', 'B', 'M', 'J', 'O', 'A'],
    ['E', 'H', 'I', 'S', 'P', 'N'],
    ['V', 'E', 'T', 'I', 'G', 'N'],
    ['B', 'A', 'L', 'I', 'Y', 'T'],
    ['E', 'Z', 'A', 'V', 'N', 'D'],
    ['R', 'A', 'L', 'E', 'S', 'C'],
    ['U', 'W', 'I', 'L', 'R', 'G'],
    ['P', 'A', 'C', 'E', 'M', 'D']
]

# Simple loop to take a value from each sublist in Dice Pool
for dice in range(len(dicePool)):
    x = random.choice(list(dicePool[dice]))
    b.insert(dice, x)

prettyBoard()

# Loop for the countdown timer when you start the program. The '\r' keeps the cursor on the same line
for i in range(countdown):
    
    print(f"Countdown: {countdown}", end='\r')
    time.sleep(1)
    countdown -= 1

print('Put those pencils down baby.')



