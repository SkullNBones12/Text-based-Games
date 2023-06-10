# My attempt at Blackjack
import random, sys

aces = ['SpadeA', 'ClubA', 'HeartA', 'DiamondA']

deck = {
    'SpadeA':11, 'Spade2': 2, 'Spade3':3, 'Spade4':4, 'Spade5':5, 'Spade6':6, 
    'Spade7':7, 'Spade8':8, 'Spade9':9, 'Spade10':10, 'SpadeJ':10, 'SpadeQ':10,
    'SpadeK':10, 'ClubA':11, 'Club2':2, 'Club3':3, 'Club4':4, 'Club5':5, 
    'Club6':6, 'Club7':7, 'Club8':8, 'Club9':9, 'Club10':10, 'ClubJ':10, 
    'ClubQ':10, 'ClubK':10, 'HeartA':11, 'Heart2':2, 'Heart3':3, 'Heart4':4, 
    'Heart5':5, 'Heart6':6, 'Heart7':7, 'Heart8':8, 'Heart9':9, 'Heart10':10, 
    'HeartJ':10, 'HeartQ':10, 'HeartK':10, 'DiamondA':11, 'Diamond2':2, 
    'Diamond3':3, 'Diamond4':4, 'Diamond5':5, 'Diamond6':6,'Diamond7':7,
    'Diamond8':8, 'Diamond9':9, 'Diamond10':10, 'DiamondJ':10, 'DiamondQ':10, 
    'DiamondK':10
}

modifiedDeck = {
    'SpadeA':11, 'Spade2': 2, 'Spade3':3, 'Spade4':4, 'Spade5':5, 'Spade6':6, 
    'Spade7':7, 'Spade8':8, 'Spade9':9, 'Spade10':10, 'SpadeJ':10, 'SpadeQ':10,
    'SpadeK':10, 'ClubA':11, 'Club2':2, 'Club3':3, 'Club4':4, 'Club5':5, 
    'Club6':6, 'Club7':7, 'Club8':8, 'Club9':9, 'Club10':10, 'ClubJ':10, 
    'ClubQ':10, 'ClubK':10, 'HeartA':11, 'Heart2':2, 'Heart3':3, 'Heart4':4, 
    'Heart5':5, 'Heart6':6, 'Heart7':7, 'Heart8':8, 'Heart9':9, 'Heart10':10, 
    'HeartJ':10, 'HeartQ':10, 'HeartK':10, 'DiamondA':11, 'Diamond2':2, 
    'Diamond3':3, 'Diamond4':4, 'Diamond5':5, 'Diamond6':6,'Diamond7':7,
    'Diamond8':8, 'Diamond9':9, 'Diamond10':10, 'DiamondJ':10, 'DiamondQ':10, 
    'DiamondK':10
}
          
playerPot = 500           
totalLost = 0
totalWon = 0
loop = 0

print('Hello and welcome to BlackJack. Your starting pot is 500.')

while True:
    
    def printTotalsPlayer():
            print(f'Player Pot: {playerPot}')
            print(f'Total Losses: {totalLost}')
            print(f'Total Winnings: {totalWon}')
            
    def endGameTotalsPlayer():
        print(f"""
                  Hands played: {loop} 
                  Total Losses: {totalLost}
                  Total Earnings: {totalWon}
                  Total take home: {playerPot}""")
    
    # Globals are bad, but cant seem to get it right w/o them
    # Takes 2 cards per player from modified deck and returns their values
    def initialHand():
        global initialCard1, initialCard2, dealerCard1, dealerCard2
        
        initialCard1 = random.choice(list(modifiedDeck.keys()))
        hand.append(initialCard1)
        usedCards.append(initialCard1)
        modifiedDeck.pop(initialCard1)
        initialCard2 = random.choice(list(modifiedDeck.keys()))
        hand.append(initialCard2)
        usedCards.append(initialCard2)
        modifiedDeck.pop(initialCard2)
        
        dealerCard1 = random.choice(list(modifiedDeck.keys()))
        dealerHand.append(dealerCard1)
        usedCards.append(dealerCard1)
        modifiedDeck.pop(dealerCard1)
        dealerCard2 = random.choice(list(modifiedDeck.keys()))
        dealerHand.append(dealerCard2)
        usedCards.append(dealerCard2)
        modifiedDeck.pop(dealerCard2)              
           
    # Main Game loop
    while playerPot  > 0:
                
        totalBet = 0
        usedCards = []
        hand = []
        handValue = 0
        dealerHand = []
        dealerHandValue = 0
        playerBust = False

        # Betting loop
        while True:
            try:
                print('Betting time.')
                playerBet = int(input())
                if playerBet < 25:
                    print('Minimum bet is 25.')
                    raise ValueError
                elif playerBet > playerPot:
                    raise ValueError
                elif playerBet != int(playerBet):
                    raise ValueError
                break
            except ValueError:
                print('Invalid')
        totalBet += playerBet
        playerPot -= playerBet

        initialHand()
        
        print('Dealer Cards: Hidden', dealerHand[1])
        
        handValue += (deck.get(initialCard1) + deck.get(initialCard2))
        dealerHandValue += (deck.get(dealerCard1) + deck.get(dealerCard2))
        
        # Stops a 22 bust if player or dealer dealth 2 Aces
        if initialCard1 and initialCard2 in aces and handValue > 21:
            handValue -= 10
            
        if dealerCard1 and dealerCard2 in aces and dealerHandValue > 21:
            dealerHandValue -= 10
    
        print(*hand, f'Total hand value: {handValue}, Total Bet: {totalBet}')
        
        # Checks for Natural BlackJacks
        if handValue == 21 and dealerHandValue != 21:
            print(*dealerHand, '-Dealer Hand')
            print('Natural blackjack. A new hand will be dealt')
            playerPot += playerBet * 2
            totalWon += playerBet
            printTotalsPlayer()
            continue
                
        elif dealerHandValue == 21 and handValue != 21:
            print(*dealerHand)
            print('Dealer Natural. A new hand will be dealt.')
            totalLost += playerBet
            printTotalsPlayer()
            continue
                    
        elif dealerHandValue == 21 and handValue == 21:
            print(dealerHand)
            print('Tie game. A new hand will be dealt.')
            playerPot += playerBet
            printTotalsPlayer()
            continue                 
        
        # Player can't play if they have no money left
        while playerPot > 0:
            
            # Try/except if they want to double, wont work if they don't have the funds
            while True:    
                doubleList = ['y', 'n']
                print('Would you like to double? (y/n)')
                try:
                    double = input()
                    if double == 'n':
                        break
                    
                    if (playerPot - playerBet) < 0:
                        raise ValueError
                    elif double not in doubleList:
                        raise ValueError
                    break
                
                except ValueError:
                    print('Invalid')
                
            if double == 'y':
                totalBet *= 2
                playerPot -= playerBet
                print(*hand, 'Total hand value: {}, Total Bet: {}'.format((handValue), totalBet))
                break
            
            else:
                print('No double bet taken.')
                break
            
        availableMoves = ['s', 'h']
        # Try/except for stand or hit
        while True:
            try:
                print("(s)tand, or (h)it?")
                playerMove = input()
                if playerMove not in availableMoves:
                    raise ValueError
                break
                
            except ValueError:
                print('Invalid')
            
        if playerMove == 's':
            print('Stand. Total: ', handValue)        
        
        elif playerMove == 'h':
            # Loop for players looking to score big
            while True:
                newPlayerCard = random.choice(list(modifiedDeck.keys()))
                hand.append(newPlayerCard)
                usedCards.append(newPlayerCard)
                modifiedDeck.pop(newPlayerCard)
                
                handValue += deck.get(newPlayerCard)        
                                    
                print(*hand, f'Hand total: {handValue}')
                
                # Blackjack   
                if handValue == 21:
                    playerPot += totalBet*2
                    totalWon += totalBet
                    printTotalsPlayer()
                    break
                
                # Multiple Aces in hand
                elif handValue > 21 and aces in hand:
                    while True:
                        aceCount = 0
                        for card in range(len(hand)):
                            if card in aces:
                                aceCount += 1
                            else:
                                aceCount += 0
                        break
                    
                    if aceCount == 1:
                        handValue -= 10
                        print('Hand total -10')
                        print(f'New Hand total: {handValue}')
                    elif aceCount == 2:
                        handValue -= 10
                        print('Hand total -10')
                        print(f'New Hand total: {handValue}')
                    elif aceCount == 3:
                        handValue -= 10
                        print('Hand total -10')
                        print(f'New Hand total: {handValue}')
                    elif aceCount == 4:
                        handValue -= 10
                        print('Hand total -10')
                        print(f'New Hand total: {handValue}')           

                # Player bust
                elif handValue > 21 and aces not in hand:
                    print('Player bust.')
                    totalLost += totalBet
                    printTotalsPlayer()
                    playerBust = True
                    break
                
                keepGoingPlayer = input('Would you like another card? (y/n)')
                
                if keepGoingPlayer == 'n':
                    print('Player stands')
                    break
        
        #Dealer's turn               
        while playerBust == False and handValue != 21:
            
            # Dealer must hit below 16
            if dealerHandValue < 16:
                newDealerCard = random.choice(list(modifiedDeck.keys()))
                dealerHand.append(newDealerCard)
                usedCards.append(newDealerCard)
                modifiedDeck.pop(newDealerCard)
                dealerHandValue += deck.get(newDealerCard)
            
            # Dealer must stand if more than 16 and less than 21    
            elif dealerHandValue > 16 and dealerHandValue < 21:
                print(*dealerHand, '-Dealer Hand')
                print('Dealer stands. Total: ', dealerHandValue)
                break
            
            # Dealer BlackJack
            elif dealerHandValue == 21:
                totalLost += totalBet
                print(*dealerHand, '-Dealer Hand')
                print('Dealer wins.')
                printTotalsPlayer()
                break
            
            # Over 21 with Aces in hand    
            elif dealerHandValue > 21 and aces in dealerHand:
                    while True:
                        aceCount = 0
                        for card in range(len(dealerHand)):
                            if card in aces:
                                aceCount += 1
                            else:
                                aceCount += 0
                        break
                    
                    if aceCount == 1:
                        dealerHandValue -= 10
                        print('Dealer Hand total -10')
                        print(f'New Hand total: {dealerHandValue}')
                        
                    elif aceCount == 2:
                        dealerHandValue -= 10
                        print('Dealer Hand total -10')
                        print(f'New Hand total: {dealerHandValue}')
                        
                    elif aceCount == 3:
                        dealerHandValue -= 10
                        print('Dealer Hand total -10')
                        print(f'New Hand total: {dealerHandValue}')
                        
                    elif aceCount == 4:
                        dealerHandValue -= 10
                        print('Dealer Hand total -10')
                        print(f'New Hand total: {dealerHandValue}')
            
            elif dealerHandValue > 21 and aces not in dealerHand:
                print(*dealerHand, '-Dealer Hand')
                print('Dealer bust.')
                playerPot += totalBet * 2
                totalWon += totalBet
                printTotalsPlayer()
                break
        
        # If neither player bust or BlackJack
        while dealerHandValue < 21 and handValue < 21:
                    
            if handValue > dealerHandValue:
                print(f"""
                    Dealer Hand Value: {dealerHandValue}
                    Player Hand Value: {handValue}""")
                print('Player wins')
                playerPot += totalBet * 2
                totalWon += totalBet
                printTotalsPlayer()
                break
            
            elif handValue < dealerHandValue:
                print(f"""
                    Dealer Hand Value: {dealerHandValue}
                    Player Hand Value: {handValue}""")
                print('Dealer wins')
                totalLost += totalBet
                printTotalsPlayer() 
                break
            
            elif dealerHandValue == handValue:
                print(f"""
                    Dealer Hand Value: {dealerHandValue}
                    Player Hand Value: {handValue}""")
                playerPot += totalBet
                printTotalsPlayer()
                break   

        loop += 1 
        
        # Player Bankrupt
        if playerPot <= 0:
            print("You've gone bankrupt! Better luck next time.")
            endGameTotalsPlayer()
            sys.exit()   
        
        # Player play again
        elif loop > 0:
            newHand = input('Keep playing (y/n): ')
            if newHand == 'y':               
                modifiedDeck = deck.copy()
                usedCards.clear()
                continue
            
            else:
                break

    endGameTotalsPlayer()

    break
                      
        
    
            
        

        
