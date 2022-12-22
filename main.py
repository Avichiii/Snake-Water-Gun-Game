import random

#main game function

def gameWin(comp, you):

    #if both player and comp chose same values then game is tie
    
    if comp == you:
        return None

    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True

    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True

    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

#this is the func where computer chose random values

print("Computer's turn: Snake(s) Water(w) or Gun(g)")
randNO = random.randint(1,3)

if randNO == 1:
    comp = 's'
elif randNO == 2:
    comp = 'w'
elif randNO == 3:
    comp = 'g'

you = input("Your Turn: Snake(s) Water(w) or Gun(g)")



c = gameWin(comp, you)

print(f"Comoputer chose {comp}")
print(f"You chose {you}")

if c == None:
    print("This game is a tie")
    with open("read.txt" , 'w') as t:
        a = t.write("No one won") 
elif c:
    print("You win")
    with open("read.txt" , 'w') as f:
        b = f.write("You won")
else:
    print("You lose") 
    with open("read.txt" , 'w') as g:
        c = g.write("comp won")
