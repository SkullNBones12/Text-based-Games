# My attempt at a MadLibs generator. Will have 10 options to choose from.

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
          up and down in it's tree. He \033[1m{c}\033[0m\033 [1m{d}\033[0m
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


    
        