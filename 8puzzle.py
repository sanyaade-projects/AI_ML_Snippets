import random
from copy import deepcopy as dc

board = ['1','2','3','8','X','4','7','6','5']
goal=['1','2','3','8','X','4','7','6','5']
pos=4

def display():
    print('\t',board[0],'|',board[1],'|',board[2])
    print('\t',board[3],'|',board[4],'|',board[5])
    print('\t',board[6],'|',board[7],'|',board[8])

def move(mov):
    global pos
    if mov == 8 and not (pos-3 < 0):
        board[pos],board[pos-3] = board[pos-3],board[pos]
        pos-=3
        display()
    if mov == 2 and not (pos > 5):
        board[pos],board[pos+3] = board[pos+3],board[pos]
        pos+=3
        display()
    if mov == 4 and not (pos%3 == 0):
        board[pos],board[pos-1] = board[pos-1],board[pos]
        pos-=1
        display()
    if mov == 6 and not (pos%3 == 2):
        board[pos],board[pos+1] = board[pos+1],board[pos]
        pos+=1
        display()

def check():
    for i in range(9):
        if board[i]!=goal[i]:
            return False
    return True

def comp(n):
    n-=1
    return n//3,n%3

def h():
    h=0
    for i in range(1,9):
        op=board.index(str(i))
        gp=goal.index(str(i))
        oi,oj = comp(op)
        gi,gj = comp(gp)
        h+=abs((gi-oi))+abs((gj-oj))
    return h

def detect_valid(board):
    p=board.index('X')
    if p%3==0:
        board.remove(4)

def AI(premov):
    #h=h()
    boardcopy = dc(board)
    if premov==8:
        #Cancel 2
        detect_valid(boardcopy)
        pass
    if premov==2:
        #Cancel 8
        pass
    if premov==4:
        #Cancel 6
        pass
    if premov==6:
        #Cancel 4
        pass

def shuffle(n):
    for i in range(n):
        c=False
        #print(random.choice([2,4,6,8]))
        while not c:
            ra=random.choice([2,4,6,8])
            print(ra)
            c=move(ra)
            print(c)
            if c==None:
                c=True

def manual():
    print('Moves:\n8: Up\n4: Left\n6: Right\n2: Down')
    display()
    print('Current Hueristic value =',h())
    while True:
        x=int(input('Move:'))
        move(x)
        print('Current Hueristic value =',h())
        gameend=check()
        if gameend:
            print('Congratulations! You won!')
            break
        if x==0:
            break

shuffle(int(input('Enter n = ')))
#print(h())
manual()