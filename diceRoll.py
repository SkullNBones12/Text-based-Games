# Dice Roller

import random

diceType = int(input('Please choose a dice type (d - 4, 6, 10, 12, 100)'))
diceNumber = int(input('Please select the number of dice'))
diceList = []

for i in range(diceNumber):
    x = range(diceType)
    y = random.choice(x) +1
    diceList.append(y)
        
print(*diceList)    