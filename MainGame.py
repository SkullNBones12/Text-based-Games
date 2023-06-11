# Attempt at game with menus

import sys, random, time 
from tabulate import tabulate

def game_1():
    '''This is the Guess the Number game. The computer will select between 1 and 10
       randomnly and give you hints. You have three guesses to complete or it kicks
       you back to the menu.
    '''

    x = random.randint(1, 10)
    total_guesses = 0

    print('Please try and and guess my secret number between 1-10!')
    # Main Game Loop
    while True:
        # Checks for integers between 1 and 10 as input
        while True:
            try:
                guess = int(input())
                if guess < 1 or guess > 10:
                    raise ValueError
                break
            except ValueError:
                print('Oops! Not a valid number. Please try again.')
        # Hints given for number
        if guess == x:
            print(f'Oh, you got me! You guessed {total_guesses} times.')
            print('You will now return to the Main Menu.')
            time.sleep(2)
            break
        elif guess > x:
            print('Your number is too high!')
        elif guess < x:
            print('Your number is too low')
        # Tallies total guesses, if three you lose
        total_guesses += 1
        if total_guesses == 3:
            print('Haha! You lose peasant!')
            print('You will now return to the Main Menu.')
            time.sleep(2)
            break

def game_2():
    '''Rock Paper Scissors baby
    '''
    # Verifies player input is a number is acceptable choice (3, 5 or 7), if not raises error
    while True:
        try:
            bestOf = int(input('How many would you like to play out of? (3, 5 or 7?): '))
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

        print('You will now return to the Main Menu.')
        time.sleep(2)
        break

def game_3():

    ''' My version of Tic-Tac-Toe with two people!
    '''

    print('Welcome to Tic-Tac-Toe. The board is numbered 0-8; 0 being the top left corner and 8 being the bottom right. Have fun!')
    
    # Starts off with empty board (dashes are to help seperate
    board = ['-'] *9
    # Main function which prints the board into a readable state
    def printBoard():
        print(f'{(board[0])}|{(board[1])}|{(board[2])}')
        print('-----')
        print(f'{(board[3])}|{(board[4])}|{(board[5])}')
        print('-----')
        print(f'{(board[6])}|{(board[7])}|{(board[8])}')

    # Main game loop
    while True:
        # This section makes sure the player only inputs integers (0-8) and the position they want to play can't overwrite another player's moves
        while True:
            try:
                player1Position = int(input('P1, Please select a place to play: '))
                if player1Position < 0 or player1Position > 8:
                    raise ValueError
                elif board[player1Position] != '-':
                    raise ValueError
                break
            except ValueError:
                print('Oops! Not a valid spot or number. Try again.')
        
        player1Choice = 'X'
        # deletes '-' character and insert's PLayer 1's 'X'
        del board[player1Position]
        board.insert((player1Position), (player1Choice))
        printBoard()
        
        # Win conditions for PLayer 1 (I'm sure there is a better way to do this)
        if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':
            print('Player 1 wins!')
            break
        elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':
            print('Player 1 wins!')
            break
        elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':
            print('Player 1 wins!')
            break
        elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X':
            print('Player 1 wins!')
            break
        elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
            print('Player 1 wins!')
            break
        elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
            print('Player 1 wins!')
            break
        elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
            print('Player 1 wins!')
            break
        elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
            print('Player 1 wins!')
            break

        if '-' not in board:
            print("Cat's game!")
            break

        # Same as Player 1's block to catch faulty inputs and prevent cell overwrites
        while True:
            try:
                player2Position = int(input('P2, Please select a place to play: '))
                if player2Position < 0 or player2Position > 8:
                    raise ValueError
                elif board[player2Position] != '-':
                    raise ValueError
                break
            except ValueError:
                print('Oops! Not a valid spot or number. Try again.')
     
        player2Choice = 'O'
        #same delete '-' and insert 'O'
        del board[player2Position]
        board.insert((player2Position), (player2Choice))
        printBoard()

        # Player 2 win conditions (could be improved)
        if board[0] == 'O' and board[1] == 'O' and board[2] == 'O':
            print('Player 2 wins!')
            break
        elif board[3] == 'O' and board[4] == 'O' and board[5] == 'O':
            print('Player 2 wins!')
            break
        elif board[6] == 'O' and board[7] == 'O' and board[8] == 'O':
            print('Player 2 wins!')
            break
        elif board[0] == 'O' and board[3] == 'O' and board[6] == 'O':
            print('Player 2 wins!')
            break
        elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
            print('Player 2 wins!')
            break
        elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
            print('Player 2 wins!')
            break
        elif board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
            print('Player 2 wins!')
            break
        elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
            print('Player 2 wins!')
            break

        if '-' not in board:
            print("Cat's game!")
            break
                
        print('You will now return to the Main Menu.')
        time.sleep(2)
        break

def game_4():
    '''My version of Mastermind board game. Does require a pip install of tabulate
       to work properly.
    '''

    # Random number generator, turns into list to compare index values
    secretCode = random.randint(1000, 10000)
    # scl is short for Secret Code list, just shorter for all the hint/win conditions
    scl = list(map(int, str(secretCode)))

    # If loops hits twelve, game exits
    loop = 0


    print("""Hello, welcome to mastermind. You will have to guess a 4 digit code chosen 
    by the computer. An 'x' means the number is in the solution but in the 
    incorrect position, a '+' means the number is in the correct position and a '/'         
    means the number is not a part of the solution.""")

    # Functions that give hints about the solutions. Can't quite figure out how to randomize it.
    def hints():
        for index in range(len(uIl)):
            if uIl[index] == scl[index]:
                hintList.append('+')
            elif uIl[index] in scl and uIl[index] != scl[index]:
                hintList.append('x')
            else:
                hintList.append('/')

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
                print('Please choose an integer between 1000-9999.')
        # uIl stands for User Input List, uIl just shorter for conditionals   
        uIl = list(map(int, str(userInput)))

        # Win condition if user input is equal to secret code
        if uIl == scl:
            print('You did it! You guessed my secret code.')
            print('You will now return to the Main Menu.')
            time.sleep(2)
            break
        
        # Game exits if 12 loops with no correct guess, like board game
        loop += 1
        
        if loop == 12:
            print('Sorry, better luck next time.')
            print('You will now return to the Main Menu.')
            time.sleep(2)
            break

        # Runs hint functions, creates pretty table with tabulate library, refreshes each loop
        while True:
            hints()
            table1 = [[f"Guess {loop}", (userInput)], [f"Hints: {hintList[-4:]}"]]
            table2.append(table1)
            print(tabulate(table2))
            break

def game_5():
    '''My attempt at a MadLibs generator. Will have 10 options to choose from.'''

    print('Hello, I generate Mad Libs. Please select a number between 1 & 10')
    print("""
        1- A Camping We Will Go!      6-  At the Arcade!
        2- My Stay at the Hospital    7-  The First Day of School
        3- Enchanted Forest           8-  In the Jungle!
        4- A day at the Zoo!          9-  Make Me A Video Game!
        5- The Fun Park               10- Vacations 
        """)

    while True:
        try:
            gameSelection = int(input())
            if gameSelection < 1 or gameSelection > 10:
                raise ValueError
            elif gameSelection != int(gameSelection):
                raise ValueError
            break
        except ValueError:
            print('Please select a number between 1 & 10.')

    def madLib1():
        print('Please fill out the following: ')
        pN1 = input('Proper Noun: ')
        n1 = input('Noun: ')
        a1 = input('Adjective (feeling): ')
        v1 = input('Verb: ')
        a2 = input('Adjective (feeling): ')
        an1 = input('Animal: ')
        v2 = input('Verb: ')
        c1 = input('Color: ')
        v3 = input('Verb (ending in -ing): ')
        av1 = input('Adverb (ending in -ly): ')
        num1 = input('Number: ')
        mot1 = input('Measure of Time: ')
        c2 = input('Color: ')
        an2 = input('Animal: ')
        num2 = input('Number: ')
        sw1 = input('Silly word: ')
        n2 = input('Noun: ')
        
        print(f"""
            This weekend I am going camping with \033[1m{pN1}\033[0m. I packed my lantern, sleeping 
            bag, and \033[1m{n1}\033[0m. I am so \033[1m{a1}\033[0m to \033[1m{v1}\033[0m in a tent. I am \033[1m{a2}\033[0m 
            we might see a \033[1m{an1}\033[0m, they are kind of dangerous. We are going to hike, fish and \033[1m{v2}\033[0m.
            I have heard that the \033[1m{c1}\033[0m lake is great for \033[1m{v3}\033[0m. Then we will \033[1m{av1}\033[0m
            hike through the forest for \033[1m{num1} {mot1}\033[0m. If I see a \033[1m{c2} {an2}\033[0m while
            hiking, I am going to bring it home as a pet! At night we will tell \033[1m{num2} {sw1}\033[0m
            stories and roast \033[1m{n2}\033[0m around the campfire!""")


    def madLib2():
        print('Please fill out the following: ')
        a = input('Number: ')
        b = input('Measure of time: ')
        c = input('Mode of Transportation: ')
        d = input('Adjective: ')
        e = input('Adjective: ')
        f = input('Noun: ')
        g = input('Color: ')
        h = input('Part of the Body: ')
        i = input('Verb: ')
        j = input('Number: ')
        k = input('Noun: ')
        l = input('Noun: ')
        m = input('Part of the Body: ')
        n = input('Verb: ')
        o = input('Noun: ')
        p = input('Adjective: ')
        q = input('Silly Word: ')
        r = input('Noun: ')
        
        print(f"""
            It was about \033[1m{a}\033[0m \033[1m{b}\033[0m ago when I came to the hospital in a \033[1m{c}\033[0m. The hospital is
            a/an \033[1m{d}\033[0m place, there are alot of \033[1m{e}\033[0m \033[1m{f}\033[0m here. There are nurses here who have 
            \033[1m{g}\033[0m \033[1m{h}\033[0m. If someone wants to come into my room I told them that they have to \033[1m{i}\033[0m
            first. I have decorated my room with \033[1m{j}\033[0m \033 \033[1m{k}\033[0m. Today a doctor came into my room and
            they were wearing a \033[1m{l}\033[0m on their \033[1m{m}\033[0m. I heard that all doctors \033[1m{n}\033[0m
            \033[1m{o}\033[0m every day for breakfast. The most \033[1m{p}\033[0m thing about being in the hospital
            is the \033[1m{q}\033[0m \033[1m{r}\033[0m!""")

    def madLib3():
        print('Please fill out the following: ')
        a = input('Proper Noun: ')
        b = input('Adjective: ')
        c = input('Color: ')
        d = input('Animal: ')
        e = input('Place: ')
        f = input('Adjective: ')
        g = input('Magical Creature (Plural): ')
        h = input('Adjective: ')
        i = input('Magical Creature (Plural): ')
        j = input('Room in a House: ')
        k = input('Noun: ')
        l = input('Noun: ')
        m = input('Noun: ')
        n = input('Adjective: ')
        o = input('Noun (Plural): ')
        p = input('Number: ')
        q = input('Measure of time: ')
        r = input('Verb (ending in ing): ')
        s = input('Adjective: ')
        t = input('Noun: ')

        print(f"""
            Dear \033[1m{a}\033[0m,
            
            I am writing to you from a \033[1m{b}\033[0m castle in an enchanted forest.
            I found myself here one day after going for a ride on a \033[1m{c}\033[0m \033[1m{d}\033[0m
            in \033[1m{e}\033[0m. There are \033[1m{f}\033[0m \033[1m{g}\033[0m and
            \033[1m{h}\033[0m \033[1m{i}\033[0m here! In the \033[1m{j}\033[0m there is a pool
            full of \033[1m{k}\033[0m. I fall asleep each night on a \033[1m{l}\033[0m
            of \033[1m{m}\033[0m and dream of \033[1m{n}\033[0m \033[1m{o}\033[0m. 
            It feels as though I have lived here for \033[1m{p}\033[0m \033[1m{q}\033[0m. I hope one day 
            you can visit, although the only way to get here now is \033[1m{r}\033[0m
            on a \033[1m{s}\033[0m \033[1m{t}\033[0m !!""")

    def madLibs4():
        print('Please fill out the following: ')
        a = input('Adjective: ')
        b = input('Noun: ')
        c = input('Verb (Past Tense): ')
        d = input('Adverb: ')
        e = input('Adjective: ')
        f = input('Noun: ')
        g = input('Noun: ')
        h = input('Adjective: ')
        i = input('Verb: ')
        j = input('Adverb: ')
        k = input('Verb (Past Tense): ')
        l = input('Adjective: ')
        
        print(f"""
            Today I went to the zoo. I saw a(n) \033[1m{a}\033[0m \033[1m{b}\033[0m jumping
            up and down in it's tree. He \033[1m{c}\033[0m \033[1m{d}\033[0m
            through the large tunnel that led to its \033[1m{e}\033[0m
            \033[1m{f}\033[0m. I got some peanuts and passed them through
            the cage to a gigantic gray \033[1m{g}\033[0m towering
            above my head. Feeding that animal made me hungry. I went to 
            get a \033[1m{h}\033[0m scoop of ice cream. It filled my stomach.
            Afterwards, I had to \033[1m{i}\033[0m \033[1m{j}\033[0m to
            catch our bus. When I got home I \033[1m{k}\033[0m
            my mom for a \033[1m{l}\033[0m day at the zoo.""")
                    
    def madLibs5():
        print('Please fill out the following: ')
        a = input('Adjective: ')
        b = input('Noun (Plural): ')
        c = input('Noun: ')
        d = input('Adverb: ')
        e = input('Number: ')
        f = input('Verb (Past-Tense): ')
        g = input('Adjective (ending in -est): ')
        h = input('Verb (Past-Tense): ')
        i = input('Adverb: ')
        j = input('Adjective: ')
        
        print(f""" 
            Today, my fabulous camp group went to a/an \033[1m{a}\033[0m
            amusement park. It was a fun park with lots of cool \033[1m{b}\033[0m
            and enjoyable play structures. When we got there,
            my kind counselor shouted loudly 'Everybody off the \033[1m{c}\033[0m.'
            We all pushed out in a terrible hurry. My
            counselor handed out yellow tickets, and we scurried in.
            I was so excited! I couldn't figure out what exciting thing
            to do first. I saw a scary roller coaster I really liked,
            so I \033[1m{d}\033[0m ran over to get in the long 
            line that had about \033[1m{e}\033[0m people in it. 
            I was \033[1m{f}\033[0m. In fact, I was so nervous my knees were
            knocking together. This was the \033[1m{g}\033[0m ride I had ever
            been on! In about two minutes I heard the crank and
            grinding of the gears. That's when the ride began! When I 
            got to the bottom. I was a little \033[1m{h}\033[0m, but I
            was proud of myself. The rest of the day went \033[1m{i}\033[0m.
            It was a/an \033[1m{j}\033[0m day at the fun park.""")

    def madLibs6():
        print('Please fill out the following: ')
        a = input('Noun (Plural): ')
        b = input('Noun (Plural): ')
        c = input('Verb: ')
        d = input('Noun: ')
        e = input('Verb (ending in -ing): ')
        f = input('Noun (Plural): ')
        g = input('Noun: ')
        h = input('Noun (Plural): ')
        
        print(f"""
            When I go to the arcade with my \033[1m{a}\033[0m there are lots of games
            to play. I apend lots of time there with my friends. In the game
            X-Men you can be different \033[1m{b}\033[0m. The point of the game is
            to \033[1m{c}\033[0m every robot. You also need to save people. Then you can
            go to the next level.
            
            In the game Star Wars you are Luke Skywalker and you try to destroy 
            every \033[1m{d}\033[0m. In a car racing/ motorcycle racing game you need
            to beat every computerized vehicle that you are \033[1m{e}\033[0m
            against.
            
            There are a whole lot of other cool games. When you play some games you win
            \033[1m{f}\033[0m for certain scores. Once your'e done you can cash
            in your tickets to get a big \033[1m{g}\033[0m. You can save your
            \033[1m{h}\033[0m for another time. When I went to ths arcade I didn't
            believe how much fun it would be. So far I have had a lot of fun
            every time I've been to this great arcade!""")
                    
    def madLibs7():
        print('Please fill out the following: ')
        a = input('Noun: ')
        b = input('Adjective: ')
        c = input('Number: ')
        d = input('Adjective: ')
        e = input('Noun: ')
        f = input('Noun (Proper): ')
        g = input('Noun (Proper): ')
        h = input('Noun (Plural): ')
        i = input('Verb (ending in -ing): ')
        j = input('Noun (Plural): ')
        k = input('Adjective: ')
        l = input('Adverb: ')
        
        print(f"""
            One very nice morning near the end of summer, my mother woke me up at
            4:00 A.M. and said, 'Wake up and smell the grass,
            sleepy head! Today is your first day of school
            and you can't be late.' I groaned in my bed for twenty seconds, but
            eventually I got dressed. I wore a blue and white striped,
            long sleeve \033[1m{a}\033[0m with a collar on it, a red tie,
            dark gray pants, white socks, black shoes, and a/an
            \033[1m{b}\033[0m hat. In ten minutes I made lunch and ate my breakfast.
            \033[1m{c}\033[0m minutes later, the bus came. A few minutes later, I was
            at school.
            
            In school, I met two really \033[1m{d}\033[0m kids. All of us became
            friends very fast. That day we had Science, and luckily my friends and
            I were at the same \033[1m{e}\033[0m. My freinds' names are
            \033[1m{f}\033[0m and \033[1m{g}\033[0m. In math we weren't together,
            and that really bugged me. We learned what \033[1m{h}\033[0m were, and 
            when to use them. At snack and recess, we played a game together. It was
            extremely fun. At P.E., we were \033[1m{i}\033[0m off of the ropes onto
            \033[1m{j}\033[0m. I thought it was a very \033[1m{k}\033[0m idea.
            In swimming class, we needed to swim extremely \033[1m{l}\033[0m, 
            or else we would have to swim longer.
            
            Befor I knew it, school was over. I grabbed all my belongings and put
            them into my backpack. In two minutes, the bus came. As I stepped into
            the bus I shouted 'Goodbye, adios amigos, and shalom,' to my friends.
            Then I went into the bus. In a flash, I was back home. This day was an extremely exciting day!""")

    def madLibs8():
        print('Please fill out the following: ')
        a = input('Adjective: ')
        b = input('Adjective: ')
        c = input('Adjective: ')
        d = input('Noun: ')
        e = input('Adjective: ')
        f = input('Adjective: ')
        g = input('Noun: ')
        h = input('Verb: ')
        i = input('Verb: ')
        j = input('Adjective: ')
        k = input('Noun: ')
        l = input('Verb: ')
        m = input('Noun: ')
        n = input('Verb: ')
        o = input('Adjective: ')
        
        print(f"""
            I walk through the color jungle. I take out my \033[1m{a}\033[0m canteen.
            There's a \033[1m{b}\033[0m parrot with a \033[1m{c}\033[0m
            \033[1m{d}\033[0m in his mouth right there in front of me
            in the \033[1m{e}\033[0m trees! I gaze at his \033[1m{f}\033[0m
            \033[1m{g}\033[0m. A sudden sound awakes me from my daydream!
            A panther's \033[1m{h}\033[0m in front of my head! I 
            \033[1m{i}\033[0m his \033[1m{j}\033[0m breath. I remember I
            have a packet of \033[1m{k}\033[0m that makes anything
            go into a deep slumber! I \033[1m{l}\033[0m it away from me in
            front of the \033[1m{m}\033[0m. Yes, he's eating it! I \033[1m{n}\033[0m away
            through the \033[1m{o}\033[0m jungle. I meet my parents at the tent.
            Phew! It's been an exciting day in the jungle.""")

    def madLibs9():
        print('Please fill out the following: ')
        a = input('Adjective: ')
        b = input('Adjective: ')
        c = input('Noun (Proper): ')
        d = input('Verb (Past-Tense): ')
        e = input('Noun (Proper): ')
        f = input('Adjective: ')
        g = input('Adjective: ')
        h = input('Noun (Plural): ')
        i = input('Large Animal: ')
        j = input('Small Animal: ')
        k = input("Girl's Name: ")
        l = input('Adjective: ')
        m = input('Noun (Plural): ')
        n = input('Adjective: ')
        o = input('Noun (Plural): ')
        p = input('Number 1-50: ')
        q = input('Noun (Proper): ')
        r = input('Number: ')
        s = input('Noun (Plural): ')
        t = input('Number: ')
        u = input('Noun (Plural): ')
        
        print(f"""
            I, the \033[1m{a}\033[0m and \033[1m{b}\033[0m \033[1m{c}\033[0m
            has \033[1m{d}\033[0m \033[1m{e}\033[0m's \033[1m{f}\033[0m
            sisters and plans to steal her \033[1m{g}\033[0m \033[1m{h}\033[0m!
            What are a \033[1m{i}\033[0m and backpacking \033[1m{j}\033[0m
            to do? Before you can help \033[1m{k}\033[0m, you'll have to collect
            the \033[1m{l}\033[0m \033[1m{m}\033[0m and \033[1m{n}\033[0m
            \033[1m{o}\033[0m that open up the \033[1m{p}\033[0m
            worlds connected to a \033[1m{q}\033[0m lair. There
            are \033[1m{r}\033[0m \033[1m{s}\033[0m and \033[1m{t}\033[0m
            \033[1m{u}\033[0m in the game, along with hundreds of other
            goodies for you to find.""")

    def madLibs10():
        print('Please fill out the following: ')
        a = input('Adjective: ')
        b = input('Adjective: ')
        c = input('Noun: ')
        d = input('Noun: ')
        e = input('Noun (Plural): ')
        f = input('Game: ')
        g = input('Noun (Plural): ')
        h = input('Verb (ending in -ing): ')
        i = input('Verb (ending in -ing): ')
        j = input('Noun (Plural): ')
        k = input('Verb (ending in -ing): ')
        l = input('Noun: ')
        m = input('Plant: ')
        n = input('Part of the Body: ')
        o = input('Place: ')
        p = input('Verb (ending in -ing): ')
        q = input('Adjective: ')
        r = input('Number: ')
        s = input('Noun (Plural ): ')
        
        print(f"""
            A vacation is when you take a trip to some \033[1m{a}\033[0m place
            with your \033[1m{b}\033[0m family. Usually you go to some place
            that is near a/an \033[1m{c}\033[0m or up on a/an \033[1m{d}\033[0m.
            A good vacation place is one where you can ride \033[1m{e}\033[0m
            or play \033[1m{f}\033[0m or go hunting for \033[1m{g}\033[0m . I like
            to spend my time \033[1m{h}\033[0m or \033[1m{i}\033[0m.
            When parents go on a vacation, they spend their time eating
            three \033[1m{j}\033[0m a day, and fathers play golf, and mothers
            sit around \033[1m{k}\033[0m. Last summer, my little brother
            fell in a/an \033[1m{l}\033[0m and got poison \033[1m{m}\033[0m all
            over his\033[1m{n}\033[0m. My family is going to go to (the)
            \033[1m{o}\033[0m, and I will practice \033[1m{p}\033[0m. Parents
            need vacations more than kids because parents are always very
            \033[1m{q}\033[0m and because they have to work\033[1m{r}\033[0m
            hours every day all year making enough \033[1m{s}\033[0m to pay
            for the vacation.""")

    if gameSelection == 1:
        madLib1()
    elif gameSelection == 2:
        madLib2()
    elif gameSelection == 3:
        madLib3()
    elif gameSelection == 4:
        madLibs4()
    elif gameSelection == 5:
        madLibs5()
    elif gameSelection == 6:
        madLibs6()
    elif gameSelection == 7:
        madLibs7()
    elif gameSelection == 8:
        madLibs8()
    elif gameSelection == 9:
        madLibs9()
    elif gameSelection == 10:
        madLibs10()
    
def game_6():
    """Hangman attempt. Are all the words correct? Hopefully."""

    print(""""
        Welcome to Hangman! Please choose a number between 
        3 && 12 for length of the word."""
        )
    # List of words that will be chosen at random based on user input
    threeLetters = [
        "aba", "abs", "ace", "act", "add", "ado", "aft", "age", "ago", "aha", "aid", "aim",
        "air", "ala", "ale", "all", "alt", "amp", "ana", "and", "ant", "any", "ape", "app",
        "apt", "arc", "are", "ark", "arm", "art", "ash", "ask", "asp", "ass", "ate", "ave",
        "awe", "axe", "aye", "BAA", "bad", "bag", "ban", "bar", "bat", "bay", "bed", "bee",
        "beg", "bel", "ben", "bet", "bid", "big", "bin", "bio", "bis", "bit", "biz", "bob",
        "bog", "boo", "bow", "box", "boy", "bra", "bud", "Bug", "bum", "bun", "bus", "but",
        "buy", "bye", "cab", "cad", "cam", "can", "cap", "car", "cat", "chi", "cob", "cod",
        "col", "con", "coo", "cop", "cor", "cos", "cot", "cow", "cox", "coy", "cry", "cub",
        "cue", "cup", "cut", "dab", "dad", "dal", "dam", "dan", "day", "Dee", "def", "del",
        "den", "dew", "did", "die", "dig", "dim", "din", "dip", "dis", "doc", "doe", "dog",
        "don", "dot", "dry", "dub", "due", "dug", "dun", "duo", "dye", "ear", "eat", "ebb",
        "ecu", "eft", "egg", "ego", "elf", "elm", "emu", "end", "era", "eta", "eve", "eye",
        "fab", "fad", "fan", "far", "fat", "fax", "fay", "fed", "fee", "fen", "few", "fig",
        "fin", "fir", "fit", "fix", "flu", "fly", "foe", "fog", "for", "fox", "fry", "fun",
        "fur", "gag", "gal", "gap", "gas", "gay", "gee", "gel", "gem", "get", "gig", "gin",
        "god", "got", "gum", "gun", "gut", "guy", "gym", "had", "ham", "has", "hat", "hay",
        "hem", "hen", "her", "hey", "hid", "him", "hip", "his", "hit", "hog", "hon", "hop",
        "hot", "how", "hub", "hue", "hug", "huh", "hum", "hut", "ice", "icy", "igg", "ill",
        "imp", "ink", "inn", "ion", "its", "ivy", "jam", "jar", "jaw", "jay", "jet", "jew",
        "job", "joe", "jog", "joy", "jug", "jun", "kay", "ken", "key", "kid", "kin", "kit",
        "lab", "lac", "lad", "lag", "lam", "lap", "law", "lax", "lay", "lea", "led", "Lee",
        "leg", "les", "let", "lib", "lid", "lie", "lip", "lit", "log", "lot", "low", "mac",
        "mad", "mag", "man", "map", "mar", "mas", "mat", "max", "may", "med", "meg", "men",
        "Met", "mid", "mil", "mix", "mob", "mod", "mol", "mom", "mon", "mop", "mot", "mud",
        "mug", "mum", "nab", "nah", "nan", "nap", "nay", "neb", "neg", "net", "new", "nil",
        "nip", "nod", "nor", "nos", "not", "now", "nun", "nut", "oak", "odd", "off", "oft",
        "oil", "old", "ole", "one", "ooh", "opt", "orb", "ore", "our", "out", "owe", "owl",
        "own", "pac", "pad", "pal", "pam", "pan", "pap", "par", "pas", "pat", "paw", "pay",
        "pea", "peg", "pen", "pep", "per", "pet", "pew", "phi", "pic", "pie", "pig", "pin",
        "pip", "pit", "ply", "pod", "pol", "pop", "pot", "pro", "psi", "pub", "pup", "put",
        "rad", "rag", "raj", "ram", "ran", "rap", "rat", "raw", "ray", "red", "ref", "reg",
        "rem", "rep", "rev", "rib", "rid", "rig", "rim", "rip", "rob", "rod", "roe", "rot",
        "row", "rub", "rue", "rug", "rum", "run", "rye", "sab", "sac", "sad", "sae", "sag",
        "sal", "sap", "sat", "saw", "say", "sea", "sec", "see", "sen", "set", "sew", "sex",
        "she", "shy", "sic", "sim", "sin", "sip", "sir", "sis", "sit", "six", "ski", "sky",
        "sly", "sod", "sol", "son", "sow", "soy", "spa", "spy", "sub", "sue", "sum", "sun",
        "sup", "tab", "tad", "tag", "tam", "tan", "tap", "tar", "tat", "tax", "tea", "ted",
        "tee", "ten", "the", "thy", "tie", "tin", "tip", "tod", "toe", "tom", "ton", "too",
        "top", "tor", "tot", "tow", "toy", "try", "tub", "tug", "two", "use", "van", "vat",
        "vet", "via", "vie", "vow", "wan", "war", "was", "wax", "way", "web", "wed", "wee",
        "wet", "who", "why", "wig", "win", "wis", "wit", "won", "woo", "wow", "wry", "wye",
        "yen", "yep", "yes", "yet", "you", "zip", "zoo"
    ]

    fourLetters = [
        'Will', 'Wife', 'Wine', 'Wind', 'West', 'Word', 'Wood', 'Work', 'Year', 'Week',
        'Area', 'Army', 'Baby', 'Back', 'Ball', 'Band', 'Bank', 'Base', 'Bill', 'Body',
        'Book', 'Call', 'Card', 'Care', 'Case', 'Cash', 'City', 'Club', 'Cost', 'Date',
        'Deal', 'Door', 'Duty', 'East', 'Edge', 'Face', 'Fact', 'Farm', 'Fear', 'Fig',
        'File', 'Film', 'Fire', 'Firm', 'Fish', 'Food', 'Foot', 'Form', 'Fund', 'Game',
        'Girl', 'Goal', 'Gold', 'Hair', 'Half', 'Hall', 'Hand', 'Head', 'Help', 'Hill',
        'Home', 'Hope', 'Hour', 'Idea', 'Jack', 'John', 'Kind', 'King', 'Lack', 'Lady',
        'Land', 'Life', 'Line', 'List', 'Look', 'Lord', 'Loss', 'Love', 'Mark', 'Mary',
        'Mind', 'Miss', 'Move', 'Name', 'Need', 'News', 'Note', 'Page', 'Pain', 'Pair',
        'Park', 'Part', 'Past', 'Path', 'Paul', 'Plan', 'Play', 'Post', 'Race', 'Rain',
        'Rate', 'Rest', 'Rise', 'Risk', 'Road', 'Rock', 'Role', 'Room', 'Rule', 'Sale',
        'Seat', 'Shop', 'Show', 'Side', 'Sign', 'Site', 'Size', 'Skin', 'Sort', 'Star',
        'Step', 'Task', 'Team', 'Term', 'Test', 'Text', 'Time', 'Tour', 'Town', 'Tree',
        'Turn', 'Type', 'Unit', 'User', 'View', 'Dese', 'Enuf', 'Feel', 'Hern', 'Hers',
        'Many', 'Mine', 'Mine', 'Much', 'Nada', 'Nish', 'None', 'Nowt', 'Ours', 'Same',
        'Self', 'Some', 'Such', 'That', 'Thee', 'Them', 'They', 'This', 'Thon', 'Thor',
        'Thou', 'Thou', 'Tone', 'What', 'Yere', 'Your', 'Will', 'Roll', 'Tend', 'Miss',
        'Vote', 'Have', 'Earn', 'Give', 'Bear', 'Step', 'Look', 'Call', 'Risk', 'Love',
        'Rest', 'Warn', 'Help', 'Pass', 'Hold', 'Find', 'Walk', 'Save', 'Sing', 'Need',
        'Face', 'Lift', 'Cope', 'Cook', 'Link', 'Shed', 'Join', 'Show', 'Cast', 'Pray',
        'Wish', 'Want', 'Know', 'Make', 'Mind', 'Slip', 'Take', 'Sign', 'Fill', 'Fail',
        'View', 'Gain', 'Lose', 'Talk', 'Hate', 'Grow', 'Seem', 'Come', 'Form', 'Draw', 
        'Land', 'Suit', 'Wait', 'Sell', 'Care', 'Rule', 'Read', 'Jump', 'Hide', 'Plan',
        'Work', 'Send', 'Ring', 'Wear', 'Pick', 'Deny', 'Name', 'Push', 'Note', 'Burn',
        'Live', 'Must', 'Mark', 'Ride', 'Feel', 'Last', 'Kill', 'Pull', 'Hang', 'Test',
        'Tell', 'Beat', 'Meet', 'Fall', 'Turn', 'Stay', 'Stop', 'Wash', 'Keep', 'Rise',
        'Shut', 'Like', 'Deal', 'Open', 'Seek', 'Vary', 'Play', 'Rely', 'Fear', 'Hurt',
        'Wake', 'Cost', 'Hear', 'Head', 'Lead', 'Sort', 'Lend', 'Dare', 'Drop', 'Blow',
        'Hope', 'Full', 'Neat', 'Grim', 'Mass', 'Deaf', 'Cold', 'Huge', 'Bare', 'Mild',
        'Firm', 'Dual', 'Okay', 'Fine', 'Just', 'Able', 'Glad', 'Easy', 'Mean', 'Bold',
        'Flat', 'Pink', 'Dark', 'Next', 'Main', 'Male', 'Last', 'Back', 'Dead', 'Damp',
        'Calm', 'Lazy', 'Hard', 'Only', 'Lone', 'Head', 'Poor', 'Late', 'Open', 'Like',
        'Loud', 'Keen', 'Holy', 'Evil', 'Mere', 'Bass', 'High', 'Blue', 'Dull', 'Live',
        'Pale', 'Fond', 'Fair', 'Foul', 'Long', 'Nazi', 'Past', 'Kind', 'Busy', 'Cool',
        'Near', 'Good', 'Oral', 'Dear', 'Half', 'Fast', 'Dumb', 'Nice', 'Deep', 'Grey',
        'Free', 'Pure', 'Rare', 'Real', 'Rear', 'Rich', 'Rude', 'Safe', 'Same', 'Sick',
        'Slim', 'Slow', 'Soft', 'Sole', 'Sore', 'Sure', 'Tall', 'Then', 'Thin', 'Tidy',
        'Tiny', 'Tory', 'True', 'Ugly', 'Vain', 'Vast', 'Very', 'Vice', 'Warm', 'Wary',
        'Weak', 'Wide', 'Wild', 'Wise', 'Zero', 'Thou', 'Till', 'When', 'Sith', 'Only',
        'Once', 'Plus', 'That', 'Save', 'Lest', 'Both', 'Like', 'Than', 'Unto', 'Then',
        'Ergo', 'Else'
    ]

    fiveLetters = [
        'About', 'Alert', 'Argue', 'Beach', 'Above', 'Alike', 'Arise', 'Began',
        'Abuse', 'Alive', 'Array', 'Begin', 'Actor', 'Allow', 'Aside', 'Begun',
        'Acute', 'Alone', 'Asset', 'Being', 'Admit', 'Along', 'Audio', 'Below',
        'Adopt', 'Alter', 'Audit', 'Bench', 'Adult', 'Among', 'Avoid', 'Billy',
        'After', 'Anger', 'Award', 'Birth', 'Again', 'Angle', 'Aware', 'Black',
        'Agent', 'Angry', 'Badly', 'Blame', 'Agree', 'Apart', 'Baker', 'Blind',
        'Ahead', 'Apple', 'Bases', 'Block', 'Alarm', 'Apply', 'Basic', 'Blood',
        'Album', 'Arena', 'Basis', 'Board', 'Boost', 'Buyer', 'China', 'Cover',
        'Booth', 'Cable', 'Chose', 'Craft', 'Bound', 'Calif', 'Civil', 'Crash',
        'Brain', 'Carry', 'Claim', 'Cream', 'Brand', 'Catch', 'Class', 'Crime',
        'Bread', 'Cause', 'Clean', 'Cross', 'Break', 'Chain', 'Clear', 'Crowd',
        'Breed', 'Chair', 'Click', 'Crown', 'Brief', 'Chart', 'Clock', 'Curve',
        'Bring', 'Chase', 'Close', 'Cycle', 'Broad', 'Cheap', 'Coach', 'Daily',
        'Broke', 'Check', 'Coast', 'Dance', 'Brown', 'Chest', 'Could', 'Dated',
        'Build', 'Chief', 'Count', 'Dealt', 'Built', 'Child', 'Court', 'Death',
        'Debut', 'Entry', 'Forth', 'Group', 'Delay', 'Equal', 'Forty', 'Grown',
        'Depth', 'Error', 'Forum', 'Guard', 'Doing', 'Event', 'Found', 'Guess',
        'Doubt', 'Every', 'Frame', 'Guest', 'Dozen', 'Exact', 'Frank', 'Guide',
        'Draft', 'Exist', 'Fraud', 'Happy', 'Drama', 'Extra', 'Fresh', 'Harry',
        'Drawn', 'Faith', 'Front', 'Heart', 'Dream', 'False', 'Fruit', 'Heavy',
        'Dress', 'Fault', 'Fully', 'Hence', 'Drill', 'Fiber', 'Funny', 'Night',
        'Drink', 'Field', 'Giant', 'Horse', 'Drive', 'Fifth', 'Given', 'Hotel',
        'Drove', 'Fifty', 'Glass', 'House', 'Dying', 'Fight', 'Globe', 'Human',
        'Eager', 'Final', 'Going', 'Ideal', 'Early', 'First', 'Grace', 'Image',
        'Earth', 'Fixed', 'Grade', 'Index', 'Eight', 'Flash', 'Grand', 'Inner',
        'Elite', 'Fleet', 'Grant', 'Input', 'Empty', 'Floor', 'Grass', 'Issue',
        'Enemy', 'Fluid', 'Great', 'Irony', 'Enjoy', 'Focus', 'Green', 'Juice',
        'Enter', 'Force', 'Gross', 'Joint', 'Judge', 'Metal', 'Media', 'Newly',
        'Known', 'Local', 'Might', 'Noise', 'Label', 'Logic', 'Minor', 'North',
        'Large', 'Loose', 'Minus', 'Noted', 'Laser', 'Lower', 'Mixed', 'Novel',
        'Later', 'Lucky', 'Model', 'Nurse', 'Laugh', 'Lunch', 'Money', 'Occur',
        'Layer', 'Lying', 'Month', 'Ocean', 'Learn', 'Magic', 'Moral', 'Offer',
        'Lease', 'Major', 'Motor', 'Often', 'Least', 'Maker', 'Mount', 'Order',
        'Leave', 'March', 'Mouse', 'Other', 'Legal', 'Music', 'Mouth', 'Ought',
        'Level', 'Match', 'Movie', 'Paint', 'Light', 'Mayor', 'Needs', 'Paper',
        'Limit', 'Meant', 'Never', 'Party', 'Peace', 'Power', 'Radio', 'Round',
        'Panel', 'Press', 'Raise', 'Route', 'Phase', 'Price', 'Range', 'Royal',
        'Phone', 'Pride', 'Rapid', 'Rural', 'Photo', 'Prime', 'Ratio', 'Scale',
        'Piece', 'Print', 'Reach', 'Scene', 'Pilot', 'Prior', 'Ready', 'Scope',
        'Pitch', 'Prize', 'Refer', 'Score', 'Place', 'Proof', 'Right', 'Sense',
        'Plain', 'Proud', 'Rival', 'Serve', 'Plane', 'Prove', 'River', 'Seven',
        'Plant', 'Queen', 'Quick', 'Shall', 'Plate', 'Sixth', 'Stand', 'Shape',
        'Point', 'Quiet', 'Roman', 'Share', 'Pound', 'Quite', 'Rough', 'Sharp',
        'Sheet', 'Spare', 'Style', 'Times', 'Shelf', 'Speak', 'Sugar', 'Tired',
        'Shell', 'Speed', 'Suite', 'Title', 'Shift', 'Spend', 'Super', 'Today',
        'Shirt', 'Spent', 'Sweet', 'Topic', 'Shock', 'Split', 'Table', 'Total',
        'Shoot', 'Spoke', 'Taken', 'Touch', 'Short', 'Sport', 'Taste', 'Tough',
        'Shown', 'Staff', 'Taxes', 'Tower', 'Sight', 'Stage', 'Teach', 'Track',
        'Since', 'Stake', 'Teeth', 'Trade', 'Sixty', 'Start', 'Texas', 'Treat',
        'Sized', 'State', 'Thank', 'Trend', 'Skill', 'Steam', 'Theft', 'Trial',
        'Sleep', 'Steel', 'Their', 'Tried', 'Slide', 'Stick', 'Theme', 'Tries',
        'Small', 'Still', 'There', 'Truck', 'Smart', 'Stock', 'These', 'Truly',
        'Smile', 'Stone', 'Thick', 'Trust', 'Smith', 'Stood', 'Thing', 'Truth',
        'Smoke', 'Store', 'Think', 'Twice', 'Solid', 'Storm', 'Third', 'Under',
        'Solve', 'Story', 'Those', 'Undue', 'Sorry', 'Strip', 'Three', 'Union',
        'Sound', 'Stuck', 'Threw', 'Unity', 'South', 'Study', 'Throw', 'Until',
        'Space', 'Stuff', 'Tight', 'Upper', 'Upset', 'Whole', 'Waste', 'Wound',
        'Urban', 'Whose', 'Watch', 'Write', 'Usage', 'Woman', 'Water', 'Wrong',
        'Usual', 'Train', 'Wheel', 'Wrote', 'Valid', 'World', 'Where', 'Yield',
        'Value', 'Worry', 'Which', 'Young', 'Video', 'Worse', 'While', 'Youth',
        'Virus', 'Worst', 'White', 'Worth', 'Visit', 'Would', 'Vital', 'Voice'
    ]

    sixLetters = [
        'Animal', 'Basket', 'Bubble', 'Butter', 'Camera', 'Carpet', 'Castle', 'Cheese',
        'Danger', 'Dragon', 'Father', 'Flower', 'Forest', 'Guitar', 'Jungle', 'Mother',
        'Orange', 'Pepper', 'Pillow', 'Planet', 'Potato', 'Rocket', 'Sailor', 'Shadow',
        'Spirit', 'Sunset', 'Tomato', 'Turtle', 'Window', 'Winter', 'Course', 'System',
        'School', 'Family', 'Market', 'Police', 'Policy', 'Office', 'Person', 'Health',
        'Period', 'Centre', 'Effect', 'Action', 'Moment', 'Report', 'Church', 'Change',
        'Street', 'Result', 'Reason', 'Nature', 'Member', 'Figure', 'Friend', 'Amount',
        'Series', 'Future', 'Labour', 'Letter', 'Theory', 'Growth', 'Chance', 'Record',
        'Energy', 'Income', 'Scheme', 'Design', 'Choice', 'Couple', 'County', 'Summer',
        'Colour', 'Season', 'Garden', 'Charge', 'Advice', 'Doctor', 'Extent', 'Access',
        'Region', 'Degree', 'Return', 'Public', 'Answer', 'Leader', 'Appeal', 'Method',
        'Source', 'Oxford', 'Demand', 'Sector', 'Status', 'Safety', 'Weight', 'League',
        'Budget', 'Review', 'Minute', 'Survey', 'Speech', 'Effort', 'Career', 'Attack',
        'Length', 'Memory', 'Impact', 'Sister', 'Corner', 'Damage', 'Credit', 'Debate',
        'Supply', 'Museum', 'Island', 'Relief', 'Target', 'Coffee', 'Factor', 'Battle',
        'Prison', 'Bridge', 'Detail', 'Client', 'Search', 'Master', 'Dinner', 'Agency',
        'Manner', 'Favour', 'Crisis', 'Prince', 'Output', 'Middle', 'Player', 'Threat',
        'Notice', 'Bottom', 'Profit', 'Second', 'Option', 'Reform', 'Spring', 'Estate',
        'Volume', 'Martin', 'Branch', 'Object', 'Driver', 'Belief', 'Murder', 'Flight',
        'Treaty', 'Desire', 'Palace', 'Engine', 'Breath', 'Screen', 'Silver', 'Injury',
        'Valley', 'Should', 'Become', 'Change', 'Appear', 'Expect', 'Ensure', 'Follow',
        'Accept', 'Remain', 'Happen', 'Create', 'Return', 'Reduce', 'Choose', 'Decide',
        'Forget', 'Listen', 'Answer', 'Enable', 'Affect', 'Obtain', 'Spread', 'Wonder',
        'Afford', 'Regard', 'Assume', 'Manage', 'Remove', 'Prefer', 'Travel', 'Attend',
        'Depend', 'Suffer', 'Notice', 'Result', 'Extend', 'Report', 'Arrive', 'Finish',
        'Secure', 'Escape', 'Assess', 'Repeat', 'Supply', 'Reveal', 'Relate', 'Retain',
        'Handle', 'Assist', 'Recall', 'Settle', 'Ignore', 'Define', 'Record', 'Bother',
        'Refuse', 'Demand', 'Reckon', 'Belong', 'Emerge', 'Intend', 'Advise', 'Defend',
        'Pursue', 'Resist', 'Impose', 'Appeal', 'Differ', 'Select', 'Attack', 'Expand',
        'Behave', 'Strike', 'Remind', 'Review', 'Employ', 'Insist', 'Switch', 'Invest',
        'Tackle', 'Gather', 'Reject', 'Inform', 'Borrow', 'Comply', 'Permit', 'Charge',
        'Commit', 'Detect', 'Excuse', 'Damage', 'Launch', 'Direct', 'Submit', 'Invite',
        'Divide', 'Engage', 'Search', 'Fulfil', 'Convey', 'Market', 'Thrust', 'Retire',
        'Adjust', 'Exceed', 'Occupy', 'Stress', 'Object', 'Please', 'Design', 'Resign',
        'Regret', 'Offset', 'Assure', 'Derive', 'Access', 'Favour', 'Cancel', 'Oppose',
        'Locate', 'Repair', 'Amount', 'Attach', 'Absorb', 'Admire', 'Combat', 'Update',
        'Modify', 'Resume', 'Render', 'Double', 'Assert', 'Defeat', 'Wander', 'Rescue',
        'Export', 'Induce', 'Figure', 'Regain', 'Devote', 'Devise', 'Govern', 'Expose',
        'Beware', 'Arrest', 'Effect', 'Murder', 'Freeze', 'Honour', 'Revive', 'Endure',
        'Insert', 'Evolve', 'Foster', 'Reform', 'Punish', 'Little', 'Social', 'Second',
        'Public', 'Likely', 'Common', 'Single', 'Former', 'Recent', 'Strong', 'Simple',
        'Modern', 'Normal', 'Soviet', 'Direct', 'Useful', 'German', 'Future', 'Senior',
        'Annual', 'Latter', 'Active', 'Middle', 'Sexual', 'Actual', 'Famous', 'Formal',
        'Proper', 'Unable', 'Lovely', 'Fourth', 'Female', 'Mental', 'Double', 'Afraid',
        'Bright', 'Bloody', 'Narrow', 'Entire', 'Severe', 'Unique', 'Guilty', 'Yellow',
        'Golden', 'Sudden', 'Global', 'Silent', 'Secret', 'Visual', 'Wooden', 'Stupid',
        'Stable', 'Honest', 'Slight', 'Remote', 'Gentle', 'Junior', 'Smooth', 'Pretty',
        'Fellow', 'Square', 'Steady', 'Bitter', 'Ethnic', 'Weekly', 'Random', 'Modest',
        'Asleep', 'Clever', 'Liable', 'Mutual', 'Nearby', 'Urgent', 'Superb', 'Strict',
        'Marine', 'Retail', 'Unfair', 'Hungry', 'Secure', 'Subtle', 'Decent', 'Bottom',
        'Lesser', 'Casual', 'Lonely', 'Fierce', 'Verbal', 'Mature', 'Absent', 'Racial',
        'Lively', 'Mobile', 'Linear', 'Orange', 'Fiscal', 'Tender', 'Eighth', 'Liquid',
        'Sacred', 'Worthy', 'Manual', 'Divine', 'Intact', 'Select', 'Tragic', 'Inland',
        'Gothic', 'Tribal', 'Ironic', 'Robust', 'Binary', 'Scarce', 'Uneven', 'Unlike',
        'Latent', 'Lethal', 'Gloomy', 'Filthy', 'Serial', 'Tricky', 'Hollow', 'Finite',
        'Coarse', 'Median', 'Baltic', 'Savage', 'Glossy', 'Racist', 'Dental', 'Inward',
        'Foster', 'Unsure', 'Feudal', 'Unpaid', 'Heroic', 'Distal', 'Inside', 'Upward',
        'Aerial', 'Triple', 'Exempt', 'Facial', 'Ritual', 'Faulty', 'Speedy', 'Lawful',
        'Floppy', 'Neural', 'Shrewd', 'Lavish', 'Rectal', 'Floral', 'Hectic', 'Arable',
        'Erotic', 'Feeble', 'Sleepy', 'Innate', 'Dorsal', 'Spinal', 'Dismal', 'Barren',
        'Meagre', 'Shabby', 'Banana', 'Bumble', 'Cactus', 'Dabble', 'Fluffy', 'Giggly',
        'Hiccup', 'Jester', 'Kaboom', 'Muppet', 'Noodle', 'Pajama', 'Quirky', 'Scooby',
        'Tickle', 'Waffle', 'Yippee', 'Zipper', 'Zoodle', 'Boogie', 'Chubby', 'Doodle',
        'Fizzle', 'Goofus', 'Hookey', 'Jumble', 'Kookie', 'Lively', 'Muddle', 'Nutmeg',
        'Puddle', 'Quacky', 'Razzle', 'Sizzle', 'Tootle', 'Wiggly', 'Yabber', 'Zephyr',
        'Zonked'
    ]

    sevenLetters = [
        'ability', 'absence', 'academy', 'account', 'accused', 'achieve',
        'acquire', 'address', 'advance', 'adverse', 'advised', 'adviser',
        'against', 'airline', 'airport', 'alcohol', 'alleged', 'already',
        'analyst', 'ancient', 'another', 'anxiety', 'anxious', 'anybody',
        'applied', 'arrange', 'arrival', 'article', 'assault', 'assumed',
        'assured', 'attempt', 'attract', 'auction', 'average', 'backing',
        'balance', 'banking', 'barrier', 'battery', 'bearing', 'beating',
        'because', 'bedroom', 'believe', 'beneath', 'benefit', 'besides',
        'between', 'billion', 'binding', 'brother', 'brought', 'burning',
        'cabinet', 'caliber', 'calling', 'capable', 'capital', 'captain',
        'caption', 'capture', 'careful', 'carrier', 'caution', 'ceiling',
        'central', 'centric', 'century', 'certain', 'chamber', 'channel',
        'chapter', 'charity', 'charlie', 'charter', 'checked', 'chicken',
        'chronic', 'circuit', 'classes', 'classic', 'climate', 'closing',
        'closure', 'clothes', 'collect', 'college', 'combine', 'comfort',
        'command', 'comment', 'compact', 'company', 'compare', 'compete',
        'complex', 'concept', 'concern', 'concert', 'conduct', 'confirm',
        'connect', 'consent', 'consist', 'contact', 'contain', 'content',
        'contest', 'context', 'control', 'convert', 'correct', 'council',
        'counsel', 'counter', 'country', 'crucial', 'crystal', 'culture',
        'current', 'cutting', 'dealing', 'decided', 'decline', 'default',
        'defence', 'deficit', 'deliver', 'density', 'deposit', 'desktop',
        'despite', 'destroy', 'develop', 'devoted', 'diamond', 'digital',
        'discuss', 'disease', 'display', 'dispute', 'distant', 'diverse',
        'divided', 'drawing', 'driving', 'dynamic', 'eastern', 'economy',
        'edition', 'elderly', 'element', 'engaged', 'enhance', 'essence',
        'evening', 'evident', 'exactly', 'examine', 'example', 'excited',
        'exclude', 'exhibit', 'expense', 'explain', 'explore', 'express',
        'extreme', 'factory', 'faculty', 'failing', 'failure', 'fashion',
        'feature', 'federal', 'feeling', 'fiction', 'fifteen', 'filling',
        'finance', 'finding', 'fishing', 'fitness', 'foreign', 'forever',
        'formula', 'fortune', 'forward', 'founder', 'freedom', 'further',
        'gallery', 'gateway', 'general', 'genetic', 'genuine', 'gigabit',
        'greater', 'hanging', 'heading', 'healthy', 'hearing', 'heavily',
        'helpful', 'helping', 'herself', 'highway', 'himself', 'history',
        'holding', 'holiday', 'housing', 'however', 'hundred', 'husband',
        'illegal', 'illness', 'imagine', 'imaging', 'improve', 'include',
        'initial', 'inquiry', 'insight', 'install', 'instant', 'instead',
        'intense', 'interim', 'involve', 'jointly', 'journal', 'journey',
        'justice', 'justify', 'keeping', 'killing', 'kingdom', 'kitchen',
        'knowing', 'landing', 'largely', 'lasting', 'leading', 'learned',
        'leisure', 'liberal', 'liberty', 'library', 'license', 'limited',
        'listing', 'logical', 'loyalty', 'machine', 'manager', 'married',
        'massive', 'maximum', 'meaning', 'measure', 'medical', 'meeting',
        'mention', 'message', 'million', 'mineral', 'minimal', 'minimum',
        'missing', 'mission', 'mistake', 'mixture', 'monitor', 'monthly',
        'morning', 'musical', 'mystery', 'natural', 'neither', 'nervous',
        'network', 'neutral', 'notable', 'nothing', 'nowhere', 'nuclear',
        'nursing', 'obvious', 'offense', 'officer', 'ongoing', 'opening',
        'operate', 'opinion', 'optical', 'organic', 'outcome', 'outdoor',
        'outlook', 'outside', 'overall', 'pacific', 'package', 'painted',
        'parking', 'partial', 'partner', 'passage', 'passing', 'passion',
        'passive', 'patient', 'pattern', 'payable', 'payment', 'penalty',
        'pending', 'pension', 'percent', 'perfect', 'perform', 'perhaps',
        'phoenix', 'picking', 'picture', 'pioneer', 'plastic', 'pointed',
        'popular', 'portion', 'poverty', 'precise', 'predict', 'premier',
        'premium', 'prepare', 'present', 'prevent', 'primary', 'printer',
        'privacy', 'private', 'problem', 'proceed', 'process', 'produce',
        'product', 'profile', 'program', 'project', 'promise', 'promote',
        'protect', 'protein', 'protest', 'provide', 'publish', 'purpose',
        'pushing', 'qualify', 'quality', 'quarter', 'radical', 'railway',
        'readily', 'Reading', 'reality', 'realize', 'receipt', 'receive',
        'recover', 'reflect', 'regular', 'related', 'release', 'remains',
        'removal', 'removed', 'replace', 'request', 'require', 'reserve',
        'resolve', 'respect', 'respond', 'restore', 'retired', 'revenue',
        'reverse', 'rollout', 'routine', 'running', 'satisfy', 'science',
        'section', 'segment', 'serious', 'service', 'serving', 'session',
        'setting', 'seventh', 'several', 'shortly', 'showing', 'silence',
        'silicon', 'similar', 'sitting', 'sixteen', 'skilled', 'smoking',
        'society', 'somehow', 'someone', 'speaker', 'special', 'species',
        'sponsor', 'station', 'storage', 'strange', 'stretch', 'student',
        'studied', 'subject', 'succeed', 'success', 'suggest', 'summary',
        'support', 'suppose', 'supreme', 'surface', 'surgery', 'surplus',
        'survive', 'suspect', 'sustain', 'teacher', 'telecom', 'telling',
        'tension', 'theatre', 'therapy', 'thereby', 'thought', 'through',
        'tonight', 'totally', 'touched', 'towards', 'traffic', 'trouble',
        'turning', 'typical', 'uniform', 'unknown', 'unusual', 'upgrade',
        'upscale', 'utility', 'variety', 'various', 'vehicle', 'venture',
        'version', 'veteran', 'victory', 'viewing', 'village', 'violent',
        'virtual', 'visible', 'waiting', 'walking', 'wanting', 'warning',
        'warrant', 'wearing', 'weather', 'webcast', 'website', 'wedding',
        'weekend', 'welcome', 'welfare', 'western', 'whereas', 'whereby',
        'whether', 'willing', 'winning', 'without', 'witness', 'working',
        'writing', 'written'
    ]

    eightLetters =[
        'ability',    'absence',    'academy',    'account',    'accused',    'achieve',    'acquire',
        'address',    'advance',    'adverse',    'advised',    'adviser',    'against',    'airline',
        'airport',    'alcohol',    'alleged',    'already',    'analyst',    'ancient',    'another',
        'anxiety',    'anxious',    'anybody',    'applied',    'arrange',    'arrival',    'article',
        'assault',    'assumed',    'assured',    'attempt',    'attract',    'auction',    'average',
        'backing',    'balance',    'banking',    'barrier',    'battery',    'bearing',    'beating',
        'because',    'bedroom',    'believe',    'beneath',    'benefit',    'besides',    'between',
        'billion',    'binding',    'brother',    'brought',    'burning',    'cabinet',    'caliber',
        'calling',    'capable',    'capital',    'captain',    'caption',    'capture',    'careful',
        'carrier',    'caution',    'ceiling',    'central',    'centric',    'century',    'certain',
        'chamber',    'channel',    'chapter',    'charity',    'charlie',    'charter',    'checked',
        'chicken',    'chronic',    'circuit',    'classes',    'classic',    'climate',    'closing',
        'closure',    'clothes',    'collect',    'college',    'combine',    'comfort',    'command',
        'comment',    'compact',    'company',    'compare',    'compete',    'complex',    'concept',
        'concern',    'concert',    'conduct',    'confirm',    'connect',    'consent',    'consist',
        'contact',    'contain',    'content',    'contest',    'context',    'control',    'convert',
        'correct',    'council',    'counsel',    'counter',    'country',    'crucial',    'crystal',
        'culture',    'current',    'cutting',    'dealing',    'decided',    'decline',    'default',
        'defence',    'deficit',    'deliver',    'density',    'deposit',    'desktop',    'despite',
        'destroy',    'develop',    'devoted',    'diamond',    'digital',    'discuss',    'disease',
        'display',    'dispute',    'distant',    'diverse',    'divided',    'drawing',    'driving',
        'dynamic',    'eastern',    'economy',    'edition',    'elderly',    'element',    'engaged',
        'enhance',    'essence',    'evening',    'evident',    'exactly',    'examine',    'example',
        'excited',    'exclude',    'exhibit',    'expense',    'explain',    'explore',    'express',
        'extreme',    'factory',    'faculty',    'failing',    'failure',    'fashion',    'feature',
        'federal',    'feeling',    'fiction',    'fifteen',    'filling',    'finance',    'finding',
        'fishing',    'fitness',    'foreign',    'forever',    'formula',    'fortune',    'forward',
        'founder',    'freedom',    'further',    'gallery',    'gateway',    'general',    'genetic',
        'genuine',    'gigabit',    'greater',    'hanging',    'heading',    'healthy',    'hearing',
        'heavily',    'helpful',    'helping',    'herself',    'highway',    'himself',    'history',
        'holding',    'holiday',    'housing',    'however',    'hundred',    'husband',    'illegal',
        'illness',    'imagine',    'imaging',    'improve',    'include',    'initial',    'inquiry',
        'insight',    'install',    'instant',    'instead',    'intense',    'interim',    'involve',
        'jointly',    'journal',    'journey',    'justice',    'justify',    'keeping',    'killing',
        'kingdom',    'kitchen',    'knowing',    'landing',    'largely',    'lasting',    'leading',
        'learned',    'leisure',    'liberal',    'liberty',    'library',    'license',    'limited',
        'listing',    'logical',    'loyalty',    'machine',    'manager',    'married',    'massive',
        'maximum',    'meaning',    'measure',    'medical',    'meeting',    'mention',    'message',
        'million',    'mineral',    'minimal',    'minimum',    'missing',    'mission',    'mistake',
        'mixture',    'monitor',    'monthly',    'morning',    'musical',    'mystery',    'natural',
        'neither',    'nervous',    'network',    'neutral',    'notable',    'nothing',    'nowhere',
        'nuclear',    'nursing',    'obvious',    'offense',    'officer',    'ongoing',    'opening',
        'operate',    'opinion',    'optical',    'organic',    'outcome',    'outdoor',    'outlook',
        'outside',    'overall',    'pacific',    'package',    'painted',    'parking',    'partial',
        'partner',    'passage',    'passing',    'passion',    'passive',    'patient',    'pattern',
        'payable',    'payment',    'penalty',    'pending',    'pension',    'percent',    'perfect',
        'perform',    'perhaps',    'phoenix',    'picking',    'picture',    'pioneer',    'plastic',
        'pointed',    'popular',    'portion',    'poverty',    'precise',    'predict',    'premier',
        'premium',    'prepare',    'present',    'prevent',    'primary',    'printer',    'privacy',
        'private',    'problem',    'proceed',    'process',    'produce',    'product',    'profile',
        'program',    'project',    'promise',    'promote',    'protect',    'protein',    'protest',
        'provide',    'publish',    'purpose',    'pushing',    'qualify',    'quality',    'quarter',
        'radical',    'railway',    'readily',    'Reading',    'reality',    'realize',    'receipt',
        'receive',    'recover',    'reflect',    'regular',    'related',    'release',    'remains',
        'removal',    'removed',    'replace',    'request',    'require',    'reserve',    'resolve',
        'respect',    'respond',    'restore',    'retired',    'revenue',    'reverse',    'rollout',
        'routine',    'running',    'satisfy',    'science',    'section',    'segment',    'serious',
        'service',    'serving',    'session',    'setting',    'seventh',    'several',    'shortly',
        'showing',    'silence',    'silicon',    'similar',    'sitting',    'sixteen',    'skilled',
        'smoking',    'society',    'somehow',    'someone',    'speaker',    'special',    'species',
        'sponsor',    'station',    'storage',    'strange',    'stretch',    'student',    'studied',
        'subject',    'succeed',    'success',    'suggest',    'summary',    'support',    'suppose',
        'supreme',    'surface',    'surgery',    'surplus',    'survive',    'suspect',    'sustain',
        'teacher',    'telecom',    'telling',    'tension',    'theatre',    'therapy',
        'thereby',    'thought',    'through',    'tonight',    'totally',    'touched',    'towards',
        'traffic',    'trouble',    'turning',    'typical',    'uniform',    'unknown',    'unusual',
        'upgrade',    'upscale',    'utility',    'variety',    'various',    'vehicle',    'venture',
        'version',    'veteran',    'victory',    'viewing',    'village',    'violent',    'virtual',
        'visible',    'waiting',    'walking',    'wanting',    'warning',    'warrant',    'wearing',
        'weather',    'webcast',    'website',    'wedding',    'weekend',    'welcome',    'welfare',
        'western',    'whereas',    'whereby',    'whether',    'willing',    'winning',    'without',
        'witness',    'working',    'writing',    'written'       
    ]

    nineLetters = [
        'ACENTRICS', 'ACICLOVIR', 'ACULEATES', 'AEROSPIKE', 'AIRBOARDS', 'AIRPROXES', 'ALLODYNIA', 'ALPHATEST', 'ANIRIDIAS', 'ANTISHAKE', 'ANTPITTAS', 'ARCHDRUID',
        'ARCHSTONE', 'ARCMINUTE', 'ARSEHOLED', 'ARTHOUSES', 'ASHTANGAS', 'AUTOMAGIC', 'AUTOREPLY', 'AUTOSAVED', 'AUTOSAVES', 'AUTOTESTS', 'AVOPARCIN', 'AZYGOUSLY',
        'BACKPLATE', 'BANDEIRAS', 'BAROTITIS', 'BASHMENTS', 'BASSLINES', 'BATTLEAXE', 'BAZZAZZES', 'BEAKERFUL', 'BEATBOXER', 'BEJESUSES', 'BHELPURIS', 'BIOENERGY',
        'BIRDSFOOT', 'BISPHENOL', 'BLEOMYCIN', 'BLINGIEST', 'BLOCKSHIP', 'BLOGRINGS', 'BLOGROLLS', 'BLOOTERED', 'BOERBULLS', 'BOLOGNESE', 'BONETIRED', 'BOOGALOOS',
        'BOTTARGAS', 'BOYSHORTS', 'BRAINFOOD', 'BREADIEST', 'BRESAOLAS', 'BRISKIEST', 'BROTHIEST', 'BROWNTAIL', 'BULLYCIDE', 'BUPROPION', 'BUZZBAITS', 'BUZZKILLS',
        'CAIRNIEST', 'CALIMOCHO', 'CALLTIMES', 'CALMSTANE', 'CAMPEACHY', 'CAMPERIES', 'CAMPHONES', 'CANCELBOT', 'CANEGRUBS', 'CAREWARES', 'CARPHONES', 'CARSHARED',
        'CARSHARES', 'CASEMIXES', 'CASEVACED', 'CATAPHORS', 'CAUMSTANE', 'CECROPINS', 'CELECOXIB', 'CERCOPIDS', 'CETUXIMAB', 'CEVITAMIC', 'CHACONINE', 'CHAMPIEST',
        'CHANTINGS', 'CHAVVIEST', 'CHECKIEST', 'CHEQUIEST', 'CHERMOULA', 'CHIMINEAS', 'CHUMASHIM', 'CLOWNFISH', 'COACHIEST', 'COCKLINGS', 'COFIRINGS', 'COMBOVERS',
        'CONSPUING', 'COPYFIGHT', 'CRANACHAN', 'CRESSIEST', 'CROREPATI', 'CRUCIATES', 'CURVINESS', 'CYCLEPATH', 'DANCICALS', 'DARKFIELD', 'DATAGRAMS', 'DAYSAILER',
        'DAYSAILOR', 'DEMOSCENE', 'DEPIGMENT', 'DEQUEUING', 'DESEEDING', 'DETANGLED', 'DETANGLER', 'DETANGLES', 'DETRUSORS', 'DIGIPACKS', 'DIPSWITCH', 'DISABLISM',
        'DISABLIST', 'DISINVENT', 'DITHIONIC', 'DOCUSOAPS', 'DONEPEZIL', 'DOORNBOOM', 'DOUGHBALL', 'DOWELINGS', 'DOWNSIZER', 'DOXAPRAMS', 'DOXASTICS', 'DRAGGINGS',
        'DREIGHEST', 'DRILLHOLE', 'DUMBSHOWS', 'DUNGHEAPS', 'DUSTCOATS', 'DYSPRAXIC', 'EASTABOUT', 'EASTLANDS', 'ECHIURANS', 'ECHOGRAPH', 'ECOLODGES', 'ECOTARIAN',
        'ECPHRASES', 'ECPHRASIS', 'EGRESSIVE', 'EMAILINGS', 'ENANTHEMA', 'ENARGITES', 'ENNEAGRAM', 'ENQUEUING', 'EPICORMIC', 'EPIMERISE', 'EPIMERIZE', 'EQUIFINAL',
        'ESCABECHE', 'EUPHRASIA', 'EUTHANASE', 'EUTHANAZE', 'EXTRUSILE', 'FACEBOOKS', 'FACIALIST', 'FALLALISH', 'FARFALLES', 'FAULTLINE', 'FEIJOADAS', 'FEMICIDAL',
        'FEMICIDES', 'FILAGGRIN', 'FLATSTICK', 'FLECKIEST', 'FLIPPIEST', 'FLIPSIDES', 'FLYPOSTER', 'FLYSPRAYS', 'FOOTBRAKE', 'FOOTPUMPS', 'FORECADDY', 'FOURPLAYS',
        'FREECYCLE', 'FREEDIVER', 'FREERIDES', 'FUCKHEADS', 'FUGGINESS', 'FUSSBALLS', 'FUZZBOXES', 'GAMEYNESS', 'GASTROPUB', 'GENOTOXIC', 'GLAMMIEST', 'GLAMPINGS',
        'GLUEBALLS', 'GLYCATION', 'GNASHINGS', 'GNATWRENS', 'GOALWARDS', 'GOLDWORKS', 'GOODFELLA', 'GOOPINESS', 'GRAPELICE', 'GRAPHENES', 'GRASSBIRD', 'GREENEYES',
        'GRENACHES', 'GREYSCALE', 'GRITTINGS', 'GROUPWORK', 'GUESTBOOK', 'GUNSIGHTS', 'GUTLESSLY', 'GUYLINERS', 'HAEREMAIS', 'HANDKNITS', 'HARDTAILS', 'HEADWALLS',
        'HEARTSINK', 'HEATWAVES', 'HELICASES', 'HEXAPODAL', 'HIERATICS', 'HINAHINAS', 'HINDCASTS', 'HONOUREES', 'HOROKAKAS', 'HOTELINGS', 'HOTELLING', 'HYPERICIN',
        'IDEOPOLIS', 'ILLAWARRA', 'IMAGINEER', 'IMPOSEXES', 'INFOTECHS', 'INGRAINER', 'INSOURCED', 'INSOURCES', 'INTEGRINS', 'INTERWEBS', 'IRUKANDJI', 'ISOPTERAN',
        'JAILBAITS', 'JASMONATE', 'JATROPHAS', 'JINKERING', 'JOINTINGS', 'JOLIOTIUM', 'KAKARIKIS', 'KALOOKIES', 'KAMOKAMOS', 'KAREAREAS', 'KAZACHOCS', 'KENNELMAN',
        'KENNELMEN', 'KEYWORKER', 'KICKFLIPS', 'KILOPONDS', 'KILOTONNE', 'KINTLEDGE', 'KITEBOARD', 'KNARLIEST', 'KOHEKOHES', 'KORIMAKOS', 'KOROMIKOS', 'KRUMPINGS',
        'KUMIKUMIS', 'KUNEKUNES', 'LABELMATE', 'LACRIMARY', 'LACTIVISM', 'LACTIVIST', 'LAMPBRUSH', 'LANDMINED', 'LANDMINES', 'LAVANDINS', 'LAWCOURTS', 'LEETSPEAK',
        'LEUCISTIC', 'LIFEHACKS', 'LINKSPANS', 'LIONHEADS', 'LIPSALVES', 'LITREAGES', 'LONGLISTS', 'LONGWORMS', 'LOUNGIEST', 'LUVVIEDOM', 'LYCAENIDS', 'MACHINIMA',
        'MACROLIDE', 'MALLCORES', 'MARKETISE', 'MARKETIZE', 'MASSTIGES', 'MATFELLON', 'MEDALPLAY', 'MELITTINS', 'MELOXICAM', 'METAFILES', 'METAVERSE', 'MICKERIES',
        'MICROBLOG', 'MIDLANDER', 'MILLHANDS', 'MIMIVIRUS', 'MINIMARTS', 'MIROMIROS', 'MOBCASTED', 'MODAFINIL', 'MOKOMOKOS', 'MONOSKIED', 'MONOTASKS', 'MOONCAKES',
        'MUCHACHAS', 'MUCKYMUCK', 'MUDHOPPER', 'MUFFETTEE', 'MULESINGS', 'MULLAHING', 'MULLERING', 'MULTITOOL', 'MUMBLIEST', 'MURRHINES', 'MYOSTATIN', 'MYSPACING',
        'NALIDIXIC', 'NANOPORES', 'NANOWIRES', 'NARGUILEH', 'NOCHELING', 'NOROVIRUS', 'NOTCHELED', 'NOUGATINE', 'NOVEMBERS', 'NUNCHUCKS', 'OECOLOGIC', 'OFFSHORED',
        'ORLISTATS', 'OSSOBUCOS', 'OVERBANKS', 'OVERCLOCK', 'OVERCLUBS', 'OVERWRAPS', 'PACIFICAE', 'PACKCLOTH', 'PACKMULES', 'PAHAUTEAS', 'PANSTICKS', 'PARALOGUE',
        'PARAPARAS', 'PARGETTER', 'PAROTIDES', 'PARURESES', 'PARURESIS', 'PERIODISE', 'PERIODIZE', 'PERMALINK', 'PERMATANS', 'PETAFLOPS', 'PHOTOCARD', 'PHOTOSHOP',
        'PIDDLIEST', 'PIERHEADS', 'PIHOIHOIS', 'PINBOARDS', 'PINOTAGES', 'PLAYDOUGH', 'PLAYSLIPS', 'PLEURONIA', 'PLINKIEST', 'POLLAXING', 'POLYAMORY', 'POPSTRELS',
        'PORCHETTA', 'PORLOCKED', 'POUFFIEST', 'POUNDINGS', 'PREMISSED', 'PROCYONID', 'PRONKINGS', 'PROPENALS', 'PROSECCOS', 'PUNCHLINE', 'PUSHBIKES', 'QUADPLAYS',    
        'QUEENFISH', 'QUOININGS', 'RAZORCLAM', 'RAZORFISH', 'REALTONES', 'REBIRTHER', 'REBLOCHON', 'RECHIPPED', 'REDRESSAL', 'REGGAETON', 'REGIFTING', 'REPEREPES',
        'REPLICANT', 'REWATERED', 'REWILDING', 'RINGETTES', 'RITUXIMAB', 'ROANPIPES', 'ROMANESCO', 'ROOTBOUND', 'ROSETTING', 'ROTOSCOPE', 'SABREWING', 'SACRALITY',
        'SAMEYNESS', 'SARKINESS', 'SCALEABLE', 'SCALEABLY', 'SCENESTER', 'SCHELLIES', 'SCHMICKER', 'SCROBBLED', 'SCROBBLES', 'SCROLLERS', 'SCUZZBAGS', 'SEANNACHY',
        'SEMIWATER', 'SEROGROUP', 'SEROTYPIC', 'SHEDHANDS', 'SHITFACES', 'SHITHOUSE', 'SHMOOZERS', 'SHMOOZIER', 'SHOPWOMAN', 'SHOPWOMEN', 'SHORTARSE', 'SHOWJUMPS',
        'SHURIKENS', 'SILYMARIN', 'SKYRMIONS', 'SLANTIEST', 'SLAPPINGS', 'SLURPIEST', 'SMACKDOWN', 'SMELLABLE', 'SMOOCHIER', 'SNOWCLONE', 'SNOWDOMES', 'SNOWGLOBE',
        'SOURVELDS', 'SPARTICLE', 'SPLICINGS', 'SPLISHING', 'SPLITTISM', 'SPLITTIST', 'SPOOFIEST', 'SPOONHOOK', 'SPOONWORM', 'SQUITTERS', 'STACATION', 'STAGETTES',
        'STAGHORNS', 'STALAGMAS', 'STAPLINGS', 'STARGAZEY', 'STEEPLING', 'STEPOVERS', 'STINKBIRD', 'STOOZINGS', 'STORMCOCK', 'STRIMMING', 'STROKABLE', 'STUMPINGS',
        'SUBPRIMES', 'SUCKHOLES', 'SUNGAZERS', 'SUNGAZING', 'SUPERFOOD', 'SUPERTRAM', 'SUPREMUMS', 'SWANSONGS', 'SWATTIEST', 'SWEARIEST', 'SWEETLIPS', 'SWEETVELD',
        'SWINGARMS', 'SWINGBINS', 'SWINGTAIL', 'SYNTHASES', 'TALKTIMES', 'TANOREXIC', 'TEALIGHTS', 'TEHSILDAR', 'TELEWORKS', 'THIEFLIKE', 'THORNBIRD', 'THREEPEAT',
        'THROWDOWN', 'TIDELINES', 'TIGERWOOD', 'TIKTAALIK', 'TIMESHARE', 'TIMESTAMP', 'TINKERMAN', 'TINKERMEN', 'TONALITIC', 'TOOSHIEST', 'TOPSCORED', 'TOPSCORES',
        'TOXOCARAL', 'TRACKBEDS', 'TRANCIEST', 'TRANSCODE', 'TRAPFALLS', 'TREKKINGS', 'TRICKSILY', 'TRIGEMINI', 'TRITANOPE', 'TRUNKWORK', 'TURDUCKEN', 'UNCLIMBED',
        'UNCOMFIER', 'UNDELETES', 'UNFANCIED', 'UNFUNNIER', 'UPMARKETS', 'UPSELLING', 'VANTBRASS', 'VAWNTIEST', 'VILLIACOS', 'VLOGGINGS', 'VODCASTED', 'VODCASTER',
        'VOLUMISER', 'VOLUMIZER', 'WANTAWAYS', 'WEBIFYING', 'WEBISODES', 'WEIGHTAGE', 'WESTABOUT', 'WHINGIEST', 'WHITELIST', 'WHOLPHINS', 'WHUPPINGS', 'WIREFRAME',
        'XERAPHINS', 'ZANAMIVIR', 'ZIPLOCKED', 'ZOLPIDEMS', 'ZWANZIGER'
    ]

    tenLetters = [
        'university', 'management', 'technology', 'government', 'department', 'categories', 'conditions', 'experience', 'activities', 'additional', 
        'washington', 'california', 'discussion', 'collection', 'conference', 'individual', 'everything', 'production', 'commercial', 'newsletter', 
        'registered', 'protection', 'employment', 'commission', 'electronic', 'particular', 'facilities', 'statistics', 'investment', 'industrial', 
        'associated', 'foundation', 'population', 'navigation', 'operations', 'understand', 'connection', 'properties', 'assessment', 'especially', 
        'considered', 'enterprise', 'processing', 'resolution', 'components', 'assistance', 'disclaimer', 'membership', 'background', 'trademarks', 
        'television', 'interested', 'throughout', 'associates', 'businesses', 'restaurant', 'procedures', 'themselves', 'evaluation', 'references', 
        'literature', 'respective', 'definition', 'networking', 'australian', 'guidelines', 'difference', 'directions', 'automotive', 'successful', 
        'publishing', 'developing', 'historical', 'scientific', 'functional', 'monitoring', 'dictionary', 'accounting', 'techniques', 'permission', 
        'generation', 'characters', 'apartments', 'designated', 'integrated', 'compliance', 'acceptance', 'strategies', 'affiliates', 'multimedia', 
        'leadership', 'comparison', 'determined', 'statements', 'completely', 'electrical', 'applicable', 'basketball', 'identified', 'frequently', 
        'laboratory', 'industries', 'expression', 'provisions', 'principles', 'compatible', 'consulting', 'recreation', 'parameters', 'introduced', 
        'originally', 'philosophy', 'regulation', 'prevention', 'healthcare', 'maintained', 'increasing', 'containing', 'guaranteed', 'convention', 
        'previously', 'conversion', 'reasonable', 'importance', 'javascript', 'objectives', 'structures', 'continuing', 'accordance', 'annotation', 
        'percentage', 'supporting', 'specialist', 'concerning', 'developers', 'equivalent', 'curriculum', 'psychology', 'appliances', 'elementary', 
        'controlled', 'authorized', 'retirement', 'efficiency', 'commitment', 'interviews', 'classified', 'confidence', 'consistent', 'securities', 
        'democratic', 'dimensions', 'contribute', 'challenges', 'submission', 'regulatory', 'inspection', 'manchester', 'continuous', 'initiative', 
        'disability', 'contractor', 'affordable', 'tournament', 'publishers', 'performing', 'absolutely', 'calculator', 'sufficient', 'resistance', 
        'candidates', 'biological', 'transition', 'instrument', 'favourites', 'relatively', 'represents', 'pittsburgh', 'revolution', 'mechanical', 
        'recognized', 'completion', 'milfhunter', 'accessible', 'birmingham', 'consultant', 'controller', 'committees', 'innovation', 'newspapers', 
        'programmes', 'eventually', 'agreements', 'innovative', 'conclusion', 'settlement', 'purchasing', 'instructor', 'bestiality', 'approaches', 
        'highlights', 'scientists', 'volunteers', 'attachment', 'calculated', 'appearance', 'parliament', 'situations', 'structural', 'prohibited', 
        'simulation', 'bankruptcy', 'substances', 'discovered', 'exhibition', 'nationwide', 'definitely', 'commentary', 'limousines', 'apparently', 
        'popularity', 'postposted', 'sacramento', 'impossible', 'depression', 'cincinnati', 'subsection', 'wallpapers', 'subsequent', 'motorcycle', 
        'disclosure', 'occupation', 'citysearch', 'atmosphere', 'experiment', 'federation', 'assignment', 'counseling', 'acceptable', 'medication', 
        'metabolism', 'personally', 'excellence', 'attributes', 'obligation', 'regardless', 'restricted', 'republican', 'attendance', 'adventures', 
        'appreciate', 'mechanisms', 'indicators', 'physicians', 'governance', 'capability', 'complaints', 'promotions', 'geographic', 'suspension', 
        'correction', 'supplement', 'admissions', 'convenient', 'displaying', 'encouraged', 'cartridges', 'automation', 'advantages', 'extensions', 
        'applicants', 'adjustment', 'treatments', 'camcorders', 'difficulty', 'collective', 'enrollment', 'interfaces', 'opposition', 'supervisor', 
        'attraction', 'customized', 'understood', 'amendments', 'attractive', 'recordings', 'polyphonic', 'adjustable', 'allocation', 'discipline', 
        'dispatched', 'installing', 'engagement', 'facilitate', 'subscriber', 'priorities', 'incredible', 'portuguese', 'everywhere', 'housewares', 
        'reputation', 'photograph', 'underlying', 'projection', 'diagnostic', 'automobile', 'downloaded', 'protective', 'sunglasses', 'preference', 
        'litigation', 'horizontal', 'ultimately', 'artificial', 'affiliated', 'activation', 'mitsubishi', 'processors', 'complexity', 'constantly', 
        'substitute', 'households', 'montgomery', 'louisville', 'algorithms', 'suggestion', 'connecting', 'proportion', 'essentials', 'protecting', 
        'separation', 'boundaries', 'luxembourg', 'deployment', 'colleagues', 'recruiting', 'prescribed', 'reproduced', 'queensland', 'addressing', 
        'discounted', 'bangladesh', 'constitute', 'graduation', 'variations', 'soundtrack', 'profession', 'separately', 'physiology', 'collecting', 
        'friendship', 'provincial', 'advertiser', 'encryption', 'possession', 'vegetables', 'thumbnails', 'respondent', 'accredited', 'compressed', 
        'scheduling', 'christians', 'impressive', 'relocation', 'violations', 'discretion', 'repository', 'generating', 'millennium', 'exceptions', 
        'macromedia', 'fellowship', 'copyrights', 'mastercard', 'chronicles', 'distribute', 'decorative', 'indigenous', 'validation', 'corruption', 
        'incentives', 'transcript', 'structured', 'reasonably', 'recommends', 'indicating', 'coordinate', 'limitation', 'widescreen', 'decorating', 
        'connectors', 'perception', 'infections', 'configured', 'analytical', 'assumption', 'technician', 'executives', 'supporters', 'withdrawal', 
        'veterinary', 'reflection', 'invitation', 'thumbzilla', 'translated', 'columnists', 'delivering', 'journalism', 'undertaken', 'identifier', 
        'conducting', 'impression', 'charleston', 'selections', 'projectors', 'vocational', 'pharmacies', 'completing', 'comparable', 'warranties', 
        'documented', 'paperbacks', 'vulnerable', 'transexual', 'mainstream', 'evaluating', 'volleyball', 'creativity', 'describing', 'quotations', 
        'behavioral', 'containers', 'screenshot', 'officially', 'consortium', 'recipients', 'traditions', 'humanities', 'britannica', 'visibility', 
        'strengthen', 'aggressive', 'determines', 'motivation', 'passengers', 'quantities', 'petersburg', 'powerpoint', 'obituaries', 'punishment', 
        'providence', 'remembered', 'wilderness', 'headphones', 'proceeding', 'volkswagen', 'subsidiary', 'terrorists', 'beneficial', 'threatened', 
        'prediction', 'ecological', 'consisting', 'submitting', 'mozambique', 'wellington', 'aboriginal', 'remarkable', 'preventing', 'productive', 
        'trackbacks', 'programmer', 'incomplete', 'legitimate', 'architects', 'unexpected', 'formatting', 'discussing', 'meaningful', 'blackberry', 
        'meditation', 'microphone', 'organizing', 'moderators', 'kazakhstan', 'kilometers', 'guarantees', 'indication', 'cigarettes', 'responding', 
        'physically', 'attempting', 'accurately', 'ministries', 'thoroughly', 'nottingham', 'identifies', 'interstate', 'systematic', 'madagascar', 
        'presenting', 'uzbekistan', 'richardson', 'fragrances', 'vocabulary', 'earthquake', 'geological', 'introduces', 'webmasters', 'acdbentity', 
        'conspiracy', 'cumulative', 'occasional', 'explicitly', 'girlfriend', 'influenced', 'complement', 'requesting', 'lauderdale', 'extraction', 
        'hypothesis', 'regression', 'collectors', 'recognised', 'azerbaijan', 'travelling', 'widespread', 'referenced', 'vietnamese', 'tremendous', 
        'surrounded', 'accomplish', 'vegetarian', 'ambassador', 'contacting', 'vegetation', 'infectious', 'continuity', 'phenomenon', 'charitable', 
        'burlington', 'researcher', 'qualifying', 'estimation', 'institutes', 'stationery', 'journalist', 'afterwards', 'signatures', 'simplified' 
    ]

    elevenLetters = [
        'amenability', 'antecedence', 'attenuation', 'abracadabra', 'nachronism', 'adventuress', 'alternately', 'antechamber', 'ambiguously', 'assignation', 'adventurism', 'alternating',
        'aphrodisiac', 'alternation', 'adventurous', 'affirmation', 'lternative', 'attestation', 'affirmative', 'adverbially', 'acrimonious', 'acupressure', 'artlessness', 'amalgamated',
        'acupuncture', 'avoirdupois', 'apostleship', 'accumulator', 'rchipelago', 'aristocracy', 'ambitiously', 'anesthetize', 'acclamation', 'anticyclone', 'approaching', 'acclimation',
        'bureaucracy', 'befittingly', 'bereavement', 'bibliophile', 'eguilement', 'bivouacking', 'benediction', 'benedictory', 'benefaction', 'blessedness', 'bombardment', 'brittleness',
        'backsliding', 'botheration', 'beneficence', 'bimetallism', 'lamelessly', 'beneficiary', 'blameworthy', 'bicarbonate', 'boysenberry', 'barbarously', 'bedevilment', 'bicentenary',
        'brilliantly', 'burgomaster', 'brotherhood', 'breastplate', 'enevolence', 'bourgeoisie', 'brusqueness', 'bashfulness', 'bloodsucker', 'bifurcation', 'beastliness', 'biliousness',
        'comportment', 'connoisseur', 'colonialism', 'copperplate', 'lassically', 'confederacy', 'connotation', 'coagulation', 'correlation', 'cartography', 'countervail', 'ceremonious',
        'confederate', 'connotative', 'correlative', 'coruscation', 'onstricted', 'countermove', 'crepuscular', 'centreboard', 'calibration', 'constrictor', 'coordinator', 'culmination',
        'coincidence', 'criminology', 'centrepiece', 'chiropodist', 'ommunistic', 'consignment', 'catheterize', 'closefisted', 'composition', 'capillarity', 'celebration', 'cobblestone',
        'describable', 'directorate', 'degradation', 'delineation', 'evastating', 'devastation', 'detestation', 'destitution', 'delinquency', 'description', 'disapproval', 'discontinue',
        'descriptive', 'distraction', 'denominator', 'dissolutely', 'islocation', 'dissolution', 'disarmament', 'disparaging', 'destruction', 'desecration', 'development', 'disillusion',
        'destructive', 'divorcement', 'discordance', 'doctrinaire', 'istressful', 'differently', 'distressing', 'diplomatist', 'disciplined', 'deliverable', 'disposition', 'evangelical',
        'edification', 'endometrium', 'elicitation', 'equivocally', 'xpropriate', 'exclusively', 'enthralling', 'efficacious', 'egotistical', 'exasperated', 'externalize', 'equivocator',
        'eligibility', 'elucidation', 'efficiently', 'explainable', 'nlargement', 'explanation', 'elimination', 'explanatory', 'editorially', 'expurgation', 'eradication', 'embrocation',
        'earnestness', 'evaporation', 'excoriation', 'encapsulate', 'nlightened', 'embroiderer', 'exquisitely', 'expatiation', 'ejaculation', 'embroilment', 'engorgement', 'forgiveness',
        'floorwalker', 'fearfulness', 'formulation', 'fascinating', 'luoroscope', 'fascination', 'feasibility', 'familiarity', 'fomentation', 'familiarize', 'fluctuating', 'fornication',
        'fluctuation', 'flexibility', 'florescence', 'fulfillment', 'ashionable', 'frustrating', 'genteelness', 'geometrical', 'gallimaufry', 'graphically', 'gravitation', 'generically',
        'garnishment', 'homesteader', 'handicapped', 'harpsichord', 'ypertrophy', 'handicapper', 'hirsuteness', 'herpetology', 'hereinafter', 'hippocampus', 'humiliating', 'humiliation',
        'hemispheric', 'housewifely', 'hydrophobia', 'independent', 'njudicious', 'innumerable', 'inflammable', 'iconography', 'intentional', 'insincerely', 'impregnable', 'insincerity',
        'interviewer', 'joblessness', 'jackhammers', 'jackknifing', 'ardinieres', 'jacobinical', 'juvenescent', 'knucklehead', 'kindhearted', 'keyboardist', 'knowingness', 'kenogenesis',
        'kinetoscope', 'kilocalorie', 'kalashnikov', 'knuckleball', 'washiorkor', 'kinesiology', 'kleptocracy', 'ketosteroid', 'kitchenmaid', 'leatherneck', 'literalness', 'lucubration',
        'landholding', 'lingeringly', 'lubrication', 'lithography', 'egislating', 'legislation', 'legislative', 'logarithmic', 'leatherette', 'marginalize', 'meritorious', 'mockingbird',
        'monasticism', 'measureless', 'misconceive', 'measurement', 'etaphysics', 'musculature', 'malingering', 'matchmaking', 'monopolizer', 'mythologist', 'massiveness', 'mythologize',
        'misconstrue', 'nationality', 'nationalize', 'nonchalance', 'umerically', 'overflowing', 'obstetrical', 'orientating', 'orientation', 'operational', 'obliqueness', 'omnipotence',
        'opinionated', 'orthopedist', 'omnipresent', 'obstruction', 'mniscience', 'originality', 'overcareful', 'opportunism', 'opportunist', 'pterodactyl', 'patriarchal', 'portraitist',
        'pornography', 'prickliness', 'portraiture', 'purposeless', 'eritonitis', 'pamphleteer', 'personality', 'putrescence', 'personalize', 'progression', 'passiveness', 'presentment',
        'pretentious', 'quadrupling', 'quicksilver', 'quarrelsome', 'uizzically', 'quotability', 'querulously', 'quarantined', 'quarterback', 'quarterdeck', 'quintillion', 'quaveringly',
        'quislingism', 'quadraphony', 'quadrasonic', 'quadrennial', 'uiescently', 'quarterlies', 'quintuplets', 'questioners', 'quantifiers', 'quantifying', 'quarantines', 'referential',
        'reformation', 'reproachful', 'reformative', 'residential', 'eformatory', 'reluctantly', 'reminiscent', 'reclamation', 'rattlesnake', 'reduplicate', 'reiteration', 'reiterative',
        'requirement', 'requisition', 'resignation', 'receptivity', 'egretfully', 'repentantly', 'resourceful', 'reverberate', 'specialized', 'stroboscope', 'seventeenth', 'springiness',
        'splintering', 'suppuration', 'septicaemia', 'straightway', 'tockbroker', 'splayfooted', 'sponsorship', 'surrounding', 'spontaneity', 'sleepwalker', 'specifiable', 'spontaneous',
        'stockholder', 'sententious', 'solidifying', 'stethoscope', 'ubmergence', 'superficial', 'substantial', 'sentimental', 'suitability', 'shepherdess', 'synergistic', 'southwester',
        'transparent', 'trapezoidal', 'tempestuous', 'transporter', 'yrannicide', 'translation', 'theoretical', 'telegrapher', 'tobogganing', 'titillating', 'telegraphic', 'titillation',
        'turbulently', 'traditional', 'typewriting', 'territorial', 'hriftiness', 'translucent', 'unessential', 'unrighteous', 'uncivilized', 'unfurnished', 'unutterable', 'utilitarian',
        'unblemished', 'unconcerned', 'unfortunate', 'utilization', 'nderground', 'unorganized', 'undergrowth', 'underhanded', 'unrepentant', 'unflinching', 'uprightness', 'unavoidable',
        'ultramarine', 'unbelieving', 'unthinkable', 'vaccinating', 'accination', 'violoncello', 'venturesome', 'viticulture', 'viscountess', 'vindication', 'vicariously', 'vermiculite',
        'vicissitude', 'vertiginous', 'whippletree', 'wheresoever', 'omanliness', 'washerwoman', 'wherewithal', 'winsomeness', 'workmanlike', 'workmanship', 'wintergreen', 'wonderfully',
        'wonderingly', 'worldliness', 'whiffletree', 'westernmost', 'heelbarrow', 'wastebasket', 'wrongheaded', 'wealthiness', 'willingness', 'woodcarving', 'witheringly', 'windbreaker',
        'worthlessly', 'windcheater', 'waggishness', 'watercolour', 'atercourse', 'xerographic', 'xylophonist', 'xanthophyll', 'xenogenesis', 'xeranthemum', 'xanthelasma', 'xenoglossia',
        'xenogenetic', 'xiphisterna', 'xiphopagous', 'xenoplastic', 'eriscaping', 'xanthomonad', 'xerographer', 'xerophagies', 'xerotripsis', 'xanthations', 'xanthophyls', 'xanthopsias',
        'xenobiotics', 'xenogeneses', 'xenophobias', 'xenophobies', 'erochasies', 'yachtswoman', 'youthquakes', 'yarboroughs', 'yuckinesses', 'yatteringly', 'yumminesses', 'yellowbacks',
        'yellowbarks', 'yellowbirds', 'yellowcakes', 'yellowheads', 'ellowwares', 'yellowweeds', 'yellowwoods', 'yellowworts', 'yersinioses', 'yersiniosis', 'yesterevens', 'yellowshins',
        'youdendrift', 'zooplankton', 'zestfulness', 'zygomorphic', 'oomorphism', 'zealousness', 'zinnwaldite', 'zoroastrian', 'zanthoxylum', 'zinciferous', 'zoophytical', 'zincography',
        'zinkiferous', 'zebrafishes', 'zygopleural', 'zeolitiform', 'oogonidium', 'zoografting', 'zygotically', 'zoomagnetic', 'zoometrical', 'zymogenesis', 'zymotechnic', 'zymotically',
        'zigzaggiest', 'zillionaire', 'zinckenites' 
    ]

    twelveLetters = [
        'astrological', 'apprehension', 'apprehensive', 'accidentally', 'appendicitis', 'adhesiveness', 'anathematize', 'accumulation', 'amalgamation', 'accumulative', 'assimilating', 'antediluvian', 'assimilation', 'announcement', 'astronomical', 'aristocratic', 'anatomically', 'administrate', 'approachable', 'alliteration', 'alliterative', 'abstractedly', 'anticipation', 'attitudinize', 'anticipatory', 'architecture', 'abstractness', 'advisability', 'augmentation', 'augmentative', 'agricultural', 'appropriator', 'abstruseness', 'arithmetical', 'allusiveness', 'alphabetical', 'bureaucratic', 'bacchanalian', 'beleaguering', 'benefactress', 'bullfighting', 'bachelorhood', 'beneficially', 'biographical', 'boisterously', 'bicentennial', 'bloodletting', 'brackishness', 'blandishment', 'bilingualism', 'bloodthirsty',    
        'breathlessly', 'backwoodsman', 'bluestocking', 'belletristic', 'bushwhacking', 'bactericidal', 'bewilderment', 'belligerence', 'belligerency', 'businesslike', 'bacteriology', 'bibliography', 'billingsgate', 'brontosaurus', 'biochemistry', 'beseechingly', 'bodybuilding', 'behaviourism', 'behaviourist', 'breakthrough', 'ceremonially', 'constraining', 'cartographer', 'condensation', 'contumacious', 'compensation', 'cancellation', 'cartographic', 'coordinately', 'contemporary', 'constricting', 'coordinating', 'constriction', 'coordination', 'contumelious', 'constrictive', 'childbearing', 'convincingly', 'coincidental', 'classifiable', 'contemptible', 'contemptibly', 'commercially', 'contemptuous', 'conviviality', 'colonization', 'childishness', 'construction', 'closemouthed', 'conciliation', 'constructive',    
        'consistently', 'conciliatory', 'counterclaim', 'chairmanship', 'disorienting', 'directorship', 'distractedly', 'divisibility', 'dissociation', 'denomination', 'dissociative', 'dethronement', 'disapproving', 'deliquescent', 'didactically', 'disfranchise', 'destructible', 'differential', 'discipleship', 'disciplinary', 'dissatisfied', 'denouncement', 'decipherable', 'distribution', 'dispossessed', 'distributive', 'dogmatically', 'disassociate', 'depopulation', 'disgorgement', 'diamagnetism', 'disinfectant', 'discouraging', 'disinfection', 'departmental', 'dispensation', 'doubtfulness', 'discourteous', 'disingenuous', 'disenchanted', 'embryologist', 'equalization', 'endangerment', 'entrancement', 'effervescent', 'effervescing', 'eavesdropper', 'encyclopedia', 'encyclopedic', 'embezzlement', 'equivocation',    
        'exasperating', 'estrangement', 'evangelistic', 'exasperation', 'enthronement', 'entreatingly', 'evisceration', 'embitterment', 'editorialize', 'enthusiastic', 'efflorescent', 'entanglement', 'entrepreneur', 'eleemosynary', 'extinguisher', 'expatriation', 'electrolysis', 'evolutionary', 'evolutionist', 'electrolytic', 'explicitness', 'emotionalism', 'enfeeblement', 'exploitation', 'fermentation', 'forestalling', 'fictionalize', 'flagellation', 'frontispiece', 'functionally', 'frangibility', 'formaldehyde', 'fundamentals', 'frankincense', 'felicitation', 'fibrillation', 'freethinking', 'fenestration', 'friendliness', 'facilitation', 'fluorescence', 'fraudulently', 'flammability', 'fainthearted', 'freakishness', 'fluorocarbon', 'fearlessness', 'feverishness', 'familiarised', 'familiarized', 'frontbencher',    
        'fruitfulness', 'frontiersman', 'faultfinding', 'fictitiously', 'flawlessness', 'figuratively', 'foreordained', 'fastidiously', 'geologically', 'genealogical', 'generational', 'gladiatorial', 'genuflection', 'governmental', 'governorship', 'galvanometer', 'geographical', 'guardianship', 'graciousness', 'gratuitously', 'geriatrician', 'gynecologist', 'globetrotter', 'gobbledygook', 'gluttonously', 'glockenspiel', 'graphologist', 'gamesmanship', 'geophysicist', 'geopolitical', 'gregariously', 'generousness', 'geochemistry', 'greathearted', 'gratefulness', 'gruesomeness', 'gratifyingly', 'gracefulness', 'gasification', 'goldbricking', 'glycogenesis', 'geometrician', 'globularness', 'gallinaceous', 'housebreaker', 'hypochondria', 'historically', 'housekeeping', 'hemstitching', 'handkerchief', 'henceforward',    
        'hypocritical', 'hierarchical', 'housewarming', 'heliocentric', 'hydrodynamic', 'hieroglyphic', 'hagiographer', 'hesitatingly', 'haberdashery', 'humorousness', 'handsomeness', 'hippopotamus', 'horsemanship', 'horizontally', 'habitability', 'hermetically', 'humanitarian', 'heartrending', 'humanization', 'hypothetical', 'hydrotherapy', 'horticulture', 'heartwarming', 'headmistress', 'hypertension', 'hypertensive', 'highlighting', 'heterosexual', 'intermission', 'inconsolable', 'intervention', 'intrauterine', 'irritability', 'intensifying', 'intermittent', 'indirectness', 'incoherently', 'illuminating', 'iconoclastic', 'illumination', 'independence', 'ineradicable', 'inarticulate', 'indiscipline', 'inflammation', 'insurrection', 'inflammatory', 'imperfection', 'incontinence', 'impregnation', 'indiscretion',    
        'infrequently', 'invigorating', 'instillation', 'intracranial', 'infringement', 'interference', 'invigoration', 'inaudibility', 'irregularity', 'incommodious', 'inauguration', 'inconvenient', 'journalistic', 'jurisdiction', 'juvenescence', 'jeopardizing', 'judicatories', 'jitterbugged', 'jeopardising', 'jeffersonian', 'jesuitically', 'judgmentally', 'juvenileness', 'journalizing', 'jurisconsult', 'jurisdictive', 'jurisprudent', 'justificator', 'judicatorial', 'jettisonable', 'juvenilities', 'journalising', 'jeopardously', 'jackanapeses', 'japonaiserie', 'juristically', 'jocularities', 'justiciaries', 'jaggednesses', 'journalisers', 'jerrymanders', 'journalizers', 'journallings', 'journeyworks', 'jailbreakers', 'jailbreaking', 'jovialnesses', 'joyfulnesses', 'kaleidoscope', 'kindergarten', 'knightliness',
        'kleptomaniac', 'karyokinesis', 'karyokinetic', 'kinaesthesis', 'kakistocracy', 'katharometer', 'katzenjammer', 'keratoplasty', 'knucklebones', 'kinaesthesia', 'kinaesthetic', 'kainogenesis', 'ketoacidosis', 'kitchenettes', 'knuckleheads', 'katamorphism', 'keratectasia', 'keratodermia', 'keratogenous', 'keratoiritis', 'keraunograph', 'keyboardists', 'kinesiatrics', 'kirschwasser', 'klipspringer', 'keratohyalin', 'ketoaciduria', 'kaleidophone', 'kilometrical', 'keratinizing', 'kinesthetics', 'knowableness', 'kiplingesque', 'legalization', 'labyrinthine', 'lexicography', 'loquaciously', 'longitudinal', 'lithographer', 'lithographic', 'longshoreman', 'legitimately', 'legitimatize', 'localization', 'liquefaction', 'lasciviously', 'lighthearted', 'lonesomeness', 'lugubriously', 'lopsidedness', 'licentiously',
        'lukewarmness', 'laboursaving', 'lifelessness', 'legitimatise', 'localisation', 'languorously', 'laundrywoman', 'listlessness', 'luminescence', 'lusciousness', 'levorotatory', 'lymphography', 'labyrinthian', 'ladylikeness', 'lexicologist', 'liturgiology', 'lepidomelane', 'laudableness', 'multifarious', 'moralization', 'misrepresent', 'maintainable', 'misapprehend', 'mysteriously', 'meetinghouse', 'misinterpret', 'ministration', 'mademoiselle', 'maximization', 'metaphysical', 'manslaughter', 'monopolistic', 'metaphorical', 'mythological', 'multilateral', 'magnetically', 'malleability', 'moderateness', 'misplacement', 'merchandiser', 'mineralogist', 'mechanically', 'merchantable', 'marriageable', 'memorability', 'manipulation', 'monosyllabic', 'manipulative', 'mulligatawny', 'magnetometer', 'monosyllable',
        'metropolitan', 'mistreatment', 'monomaniacal', 'nonexistence', 'nonconductor', 'northwestern', 'nonsensitive', 'neurasthenia', 'notification', 'noncombatant', 'nonessential', 'noncommittal', 'negativeness', 'navigability', 'nonchalantly', 'nomenclature', 'nonresistant', 'neurological', 'naturalistic', 'northeastern', 'nasalization', 'novelization', 'nonagenarian', 'northernmost', 'neighborhood', 'nonfictional', 'nonalcoholic', 'nonabsorbent', 'nonalignment', 'neurasthenic', 'newspaperman', 'nonflammable', 'neuroscience', 'nonexplosive', 'narcissistic', 'nonflowering', 'neurosurgeon', 'neurosurgery', 'neurotically', 'ostentatious', 'obsolescence', 'orthographic', 'obligatorily', 'obstetrician', 'occupational', 'obstreperous', 'omnipresence', 'obliteration', 'overestimate', 'oceanography', 'overexertion',
        'overreaching', 'organization', 'octogenarian', 'overwhelming', 'officeholder', 'onomatopoeia', 'onomatopoeic', 'outmanoeuvre', 'obscurantism', 'obscurantist', 'overcautious', 'overpowering', 'oligarchical', 'obsequiously', 'ossification', 'occasionally', 'overachiever', 'outstretched', 'orthopaedics', 'orthopaedist', 'overemphasis', 'otherworldly', 'outlandishly', 'optimization', 'perverseness', 'pleasantness', 'persistently', 'presentation', 'pumpernickel', 'passionately', 'patriarchate', 'pornographic', 'protuberance', 'partisanship', 'paleontology', 'praiseworthy', 'petrifaction', 'principality', 'putrefaction', 'partitioning', 'putrefactive', 'premeditated', 'prevaricator', 'preponderant', 'presentiment', 'preponderate', 'prolongation', 'propitiation', 'prerequisite', 'propitiatory', 'preventative',
        'penitentiary', 'preservation', 'professional', 'preservative', 'phrenologist', 'preconceived', 'protestation', 'preposterous', 'processional', 'quarterstaff', 'quintessence', 'questionable', 'questionably', 'quantitative', 'quadrangular', 'quixotically', 'quadriplegia', 'quadriplegic', 'quantifiable', 'quantization', 'quadraphonic', 'quarterfinal', 'quinquennium', 'quantisation', 'quarterlight', 'quadriphonic', 'quattrocento', 'quarantining', 'quadrenniums', 'quadricepses', 'quadrillions', 'questionings', 'quantitation', 'quarterbacks', 'quarterdecks', 'quelquechose', 'quinquennial', 'quadriennial', 'qualificator', 'quadrinomial', 'questionless', 'quantitively', 'quadrivalent', 'quantivalent', 'quaquaversal', 'relationship', 'reinvigorate', 'rhythmically', 'resoluteness', 'repatriation', 'renunciation',
        'receivership', 'reminiscence', 'reenlistment', 'restaurateur', 'reconcilable', 'radiographer', 'reproduction', 'recuperative', 'reproductive', 'redistribute', 'repercussion', 'reticulation', 'regeneration', 'resurrection', 'racketeering', 'recalcitrant', 'retrenchment', 'repossession', 'resuscitator', 'respectively', 'recognizable', 'rejuvenation', 'recognizance', 'remonstrance', 'rhododendron', 'ratification', 'reassessment', 'refrigerator', 'rightfulness', 'reassignment', 'spermatozoon', 'satisfaction', 'staggeringly', 'scandalously', 'southeastern', 'satisfactory', 'statistician', 'straightness', 'sarsaparilla', 'satisfyingly', 'southernmost', 'sleepwalking', 'supervention', 'specifically', 'swashbuckler', 'slovenliness', 'slipperiness', 'southwestern', 'subcommittee', 'substantiate', 'surveillance',
        'shuffleboard', 'stenographer', 'successively', 'stenographic', 'superannuate', 'segmentation', 'subjectivity', 'semiprecious', 'sharpshooter', 'subscription', 'substituting', 'steeplechase', 'stereoscopic', 'substitution', 'sexagenarian', 'tercentenary', 'transgressor', 'testamentary', 'tractability', 'transcendent', 'triumphantly', 'transitional', 'translatable', 'triglyceride', 'terrifically', 'tradespeople', 'telegraphist', 'thanksgiving', 'transduction', 'translucence', 'translucency', 'thoroughbred', 'thoroughfare', 'tangentially', 'trigonometry', 'thoroughness', 'theosophical', 'transmigrate', 'transferable', 'transference', 'transmission', 'thermometric', 'therapeutics', 'tuberculosis', 'teleological', 'transmitting', 'transmogrify', 'thundercloud', 'typification', 'technicality', 'transmutable',
        'unreservedly', 'untimeliness', 'unquestioned', 'unlikelihood', 'unlikeliness', 'universalism', 'universalist', 'unparalleled', 'universality', 'universalize', 'unconsidered', 'unmistakable', 'unsuccessful', 'unprincipled', 'unacceptable', 'unauthorized', 'ungainliness', 'unscrupulous', 'uncharitable', 'undercurrent', 'unseasonable', 'unbelievable', 'unseasonably', 'uninterested', 'ungovernable', 'unaccustomed', 'unprofitable', 'unregenerate', 'unfrequented', 'unacquainted', 'unanswerable', 'untrammelled', 'unprejudiced', 'unreasonable', 'unemployable', 'unemployment', 'vilification', 'vitalization', 'venerability', 'vocalization', 'vaporization', 'vociferation', 'veterinarian', 'vainglorious', 'vituperation', 'vituperative', 'victoriously', 'vitalisation', 'voluptuously', 'virtuousness', 'varicoloured',
        'vibraphonist', 'verification', 'vaudevillian', 'vocalisation', 'vindictively', 'vocationally', 'vociferously', 'volumetrical', 'vaporisation', 'variableness', 'vivification', 'vesiculation', 'valetudinary', 'volcanically', 'vaticination', 'vanquishable', 'viscosimeter', 'vermiculated', 'valuableness', 'verticalness', 'vaporousness', 'whimsicality', 'weatherboard', 'wretchedness', 'weatherproof', 'wainscotting', 'watchfulness', 'welterweight', 'whippoorwill', 'weightlifter', 'warmongering', 'waterproofed', 'wholehearted', 'wrongfulness', 'wastefulness', 'whortleberry', 'weatherglass', 'wollastonite', 'warehouseman', 'womanishness', 'windlessness', 'weisenheimer', 'woolgatherer', 'walkingstick', 'withstanding', 'weatherstrip', 'whitewashing', 'woodcarvings', 'wheelwrights', 'wallpapering', 'weathercocks',
        'wisecracking', 'watercourses', 'weightlessly', 'wildernesses', 'workingwoman', 'workingwomen', 'xylophonists', 'xiphisternum', 'xanthochroic', 'xanthochroid', 'xanthomatous', 'xylobalsamum', 'xerodermatic', 'xeromorphous', 'xanthochroia', 'xanthopterin', 'xiphiplastra', 'xanthophylls', 'xenodochiums', 'xenoglossias', 'xenoglossies', 'xeranthemums', 'xerographers', 'xerographies', 'xerophytisms', 'xiphopaguses', 'xylographers', 'xylographies', 'xylographing', 'xiphisternal', 'xenoparasite', 'xenosauridae', 'xerophthalmy', 'xanthogenate', 'xenopeltidae', 'xiphosternum', 'xiphosuridae', 'xenophontean', 'xenophontian', 'xenophontine', 'xenophoridae', 'xenopterygii', 'yellowhammer', 'youthfulness', 'yellowthroat', 'youngberries', 'yieldingness', 'yeastinesses', 'yellownesses', 'yesternights', 'yoctoseconds',
        'yamoussoukro', 'yellowshanks', 'yorkshireism', 'yorkshireman', 'yearnfulness', 'younghearted', 'youthfullity', 'yachtmanship', 'yezdegerdian', 'yarovization', 'yaroslavskiy', 'yttrocrasite', 'yttrogummite', 'yablonovskiy', 'yokeableness', 'yugoslavians', 'yazdegerdian', 'yellowjacket', 'zygomorphous', 'zoologically', 'zoophytology', 'zincographer', 'zygapophysis', 'zygodactylic', 'zoochemistry', 'zoogeography', 'zoographical', 'zalambdodont', 'zantedeschia', 'zoopathology', 'zincographic', 'zoospermatic', 'zoosporangia', 'zygapophyses', 'zootechnical', 'zinjanthropi', 'zootomically', 'zooxanthella', 'zygomycetous', 'zygomorphism', 'zoomagnetism', 'zwitterionic', 'zymotechnics', 'zoomastigote', 'zillionaires', 'zoantharians', 'zoanthropies', 'zoograftings', 'zoographists', 'zoomorphisms', 'zanthoxylums',
        'zooplankters', 'zooplanktons', 'zootherapies', 'backwardness', 'cryptography', 'enthrallment', 'faithfulness', 'hairsplitter', 'insalubrious'
    ]
    
    # Hangman pics for wrong guesses
    emptyStart = """
            ____
                |
                |
                |        
                |
                |
            ____|____
            
    """
    wrongGuess1 = """
            ____
           |    |
                |
                |        
                |
                |
            ____|____
            
    """
    wrongGuess2 = """
            ____
           |    |
           o    |
                |        
                |
                |
            ____|____
            
    """
    wrongGuess3 = """
            ____
           |    |
           o    |
           |    |        
                |
                |
            ____|____
            
    """
    wrongGuess4 = """
            ____
           |    |
           o    |
          /|    |        
                |
                |
            ____|____
            
    """
    wrongGuess5 = """
            ____
           |    |
           o    |
          /|\   |        
                |
                |
            ____|____
            
    """
    wrongGuess6 = """
            ____
           |    |
           o    |
          /|\   |        
          /     |
                |
            ____|____
            
    """
    wrongGuess7 = """
            ____
           |    |
           o    |
          /|\   |        
          / \   |
                |
            ____|____
            
    """

    # List for hangman pics
    hangmanPics = [emptyStart, wrongGuess1, wrongGuess2, wrongGuess3, 
                wrongGuess4, wrongGuess5, wrongGuess6, wrongGuess7
    ]
    # List to choose which length of letters for random word
    masterList = [threeLetters, fourLetters, fiveLetters, 
                sixLetters,sevenLetters, eightLetters, nineLetters,
                tenLetters, elevenLetters, twelveLetters
    ]
    # Loop is increased by one for each wrong guess
    loop = 0
    #Main Game Loop
    while True:
        # Get length of random word
        while True:
            try:
                lengthChoice = int(input())
                if lengthChoice < 3 or lengthChoice > 12:
                    raise ValueError
                randomWord = random.choice(masterList[lengthChoice - 3])
                break
            except ValueError:
                print("Please enter a number between 3 && 12.")
        
        wordList = list(randomWord.lower())
        # Create blank list for guesses
        guessList = ['_'] * lengthChoice
        alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
                        'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r',
                        's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
        usedLetters = []
        # Where main game logic runs     
        while True:
            if loop == 7:
                print(hangmanPics[loop])
                print(f'You have run out of guesses. The word was {randomWord}.')
                print('You will now return to the Main Menu.')
                time.sleep(2)
                break
            elif guessList == wordList:
                print("You have guessed the word. Congratulations!")
                print('You will now return to the Main Menu.')
                time.sleep(2)
                break
                        
            print(hangmanPics[loop])
            print(*guessList)
            print('--------------------------------')
            print('Used letters: ' )
            print(*usedLetters)
            print('Please enter your guess: ')
            
            while True:
                # Block for checking letter isnt used, in the alphabet and not greater than 1 letter
                try:
                    x = input()  
                    if len(x) != 1:
                        raise ValueError
                    elif x in usedLetters:
                        raise ValueError
                    elif x not in alphabetList:
                        raise ValueError
                    elif x != str(x):
                        raise ValueError
                    usedLetters.append(x)
                    break
                except ValueError:
                    print('Please enter an unused letter from the alphabet.')
            
            if x not in wordList:
                print('Not in the word.')
                loop += 1
            # Iterates through wordList and checks if the letter is in the wordList, and inserts the letter into the guessList
            elif x in wordList:
                for i in range(len(wordList)):
                    if x == wordList[i]:
                        del guessList[i]
                        guessList.insert(i, x)           
        
        break 
                    
def game_7():
    '''My attempt at Blackjack'''

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
                      
def game_8():
    # Boggle board
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
        
def game_9():
    '''Dice Roller'''

    diceType = int(input('Please choose a dice type (d - 4, 6, 10, 12, 100)'))
    diceNumber = int(input('Please select the number of dice'))
    diceList = []

    for i in range(diceNumber):
        x = range(diceType)
        y = random.choice(x) +1
        diceList.append(y)
            
    print(*diceList)    
        
def game_10():
    '''Tower of Hanoi attempt'''

    # Tower Lists
    t = [8, 7, 6, 5, 4, 3, 2, 1]
    m = []
    b = []

    loops = 0

    def towerPrint():
        print('Top- ',*t) 
        print('Mid- ',*m) 
        print('Bot- ',*b)

    # While the winning condition is not true
    while b!= [8,7,6,5,4,3,2,1]:
        
        if loops == 0:
            print('Welcome to the Tower of Hanoi! Good Luck!')
            towerPrint()
            
        while True:
            x = input('Move disc from (t, m, b): ')
            y = input('Move disc to (t, m, b): ')
            
            # Try section that restricts the movement of the discs
            try:
                if x == y: 
                    raise ValueError
                elif x == 't' and y == 'm':
                    if m == []:
                        break
                    elif t[-1] > m[-1]:
                        raise ValueError
                elif x == 't' and y == 'b':
                    if b == []:
                        break
                    elif t[-1] > b[-1]:
                        raise ValueError
                
                elif x == 'm' and y == 't':
                    if t == []:
                        break
                    elif m[-1] > t[-1]:
                        raise ValueError
                elif x == 'm' and y == 'b':
                    if b == []:
                        break
                    elif m[-1] > b[-1]:
                        raise ValueError
                    
                elif x == 'b' and y == 'm':
                    if m == []:
                        break
                    elif b[-1] > m[-1]:
                        raise ValueError
                elif x == 'b' and y == 't':
                    if t == []:
                        break
                    elif b[-1] > t[-1]:
                        raise ValueError
                
                break
                
            except ValueError:
                print('Invalid move')
        
        # Appends to the lists for the tower that get printed out and removes moved piece
        if x == 't':
        
            if y == 'm':
                m.append(t[-1])
                t.remove(t[-1])              
                
            elif y == 'b':
                b.append(t[-1])
                t.remove(t[-1])
                
        elif x == 'm':
        
            if y == 't':
                t.append(m[-1])
                m.remove(m[-1])              
                
            elif y == 'b':
                b.append(m[-1])
                m.remove(m[-1])
                
        elif x == 'b':
        
            if y == 't':
                t.append(b[-1])
                b.remove(b[-1])              
                
            elif y == 'm':
                m.append(b[-1])
                b.remove(b[-1])    
        
                
        towerPrint()
        
        loops += 1

    print(f'You have solved the puzzle in {loops} loops!')        

# Main Menu Game Selection

while True:
    print("Hello, please choose a game to play!")
    print("""
    Guess the Number        -1  Hangman        -6
    Rock, Paper, Scissors   -2  BlackJack      -7
    Tic-Tac-Toe             -3  Boggle         -8
    Mastermind              -4  Dice Roller    -9
    Madlibs                 -5  Tower of Hanoi -10
          
    Quit                    -q
    """)

    # Main menu loop where you choose a game
    while True:
        exit_game = input('Play (enter), or (q)uit? ')
        if exit_game == 'q':
            sys.exit()
        try:
            game_select = int(input('1-10: '))
            if game_select not in range(1, 11):
                raise ValueError
            break
        except ValueError:
            print('Please input only numbers 1-10.')

    if game_select == 1:
        game_1()
    elif game_select == 2:
        game_2()
    elif game_select == 3:
        game_3()
    elif game_select == 4:
        game_4()
    elif game_select == 5:
        game_5()
    elif game_select == 6:
        game_6()
    elif game_select == 7:
        game_7()
    elif game_select == 8:
        game_8()
    elif game_select == 9:
        game_9()
    elif game_select == 10:
        game_10()
