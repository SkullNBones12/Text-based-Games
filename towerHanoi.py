# Tower of Hanoi



t = [8, 7, 6, 5, 4, 3, 2, 1]
m = []
b = []

loops = 0

def towerPrint():
    print('Top- ',*t) 
    print('Mid- ',*m) 
    print('Bot- ',*b)

while b!= [8,7,6,5,4,3,2,1]:
    
    if loops == 0:
        print('Welcome to the Tower of Hanoi! Good Luck!')
        towerPrint()
        
    while True:
        x = input('Move disc from (t, m, b): ')
        y = input('Move disc to (t, m, b): ')
        
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