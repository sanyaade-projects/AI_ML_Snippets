import random
from copy import deepcopy as dc

goal=['1','2','3','8','X','4','7','6','5']

def comp(n):
    return n//3,n%3

class Node:
    def __init__(self,board,level):
        self.board = board
        self.pos = self.board.index('X')
        self.successor = []
        self.level = level
    
    def display(self):
        board = self.board
        print('\t',board[0],'|',board[1],'|',board[2])
        print('\t',board[3],'|',board[4],'|',board[5],'\t|',self.h(),'|')
        print('\t',board[6],'|',board[7],'|',board[8],'\n\n')
    
    def move(self,mov):
        board = self.board
        pos = self.pos
        if mov == 8 and not (pos-3 < 0):
            board[pos],board[pos-3] = board[pos-3],board[pos]
            pos-=3
        if mov == 2 and not (pos > 5):
            board[pos],board[pos+3] = board[pos+3],board[pos]
            pos+=3
        if mov == 4 and not (pos%3 == 0):
            board[pos],board[pos-1] = board[pos-1],board[pos]
            pos-=1
        if mov == 6 and not (pos%3 == 2):
            board[pos],board[pos+1] = board[pos+1],board[pos]
            pos+=1
    
    def h(self):
        board = self.board
        h=0
        for i in range(1,9):
            op=board.index(str(i))
            gp=goal.index(str(i))
            oi,oj = comp(op)
            gi,gj = comp(gp)
            h+=abs((gi-oi))+abs((gj-oj))
        return h

def simple_hill_climb(root):
    goalpath.append(root)
    for i in [2,4,6,8]:
        newnode = Node(dc(root.board),root.level+1)
        newnode.move(i)
        if newnode.board!=root.board:
            root.successor.append(newnode)
            if newnode.h() < root.h():
                #newnode.display()
                if newnode.h() == 0:
                    goalpath.append(newnode)
                    return
                return simple_hill_climb(newnode)

def AI():
    #h=h()
    board = ['1','2','3','8','X','4','7','6','5']
    root = Node(board,0)
    for i in [2,4,6,8]:
        print(i)
        newnode = Node(dc(root.board),root.level+1)
        newnode.move(i)
        if newnode.board!=root.board:
            root.successor.append(newnode)
        else:
            del newnode
    print('Root --->')
    root.display()
    print(len(root.successor))
    for i in range(len(root.successor)):
        print('Successor', i,'--->')
        root.successor[i].display()

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

#shuffle(int(input('Enter n = ')))
#print(h())
#manual()
#AI()
board=['2','8','3','1','6','4','7','X','5']
root=Node(board,0)
print('Initial State --->\n\n')
root.display()
print('Path followed --->\n\n')
goalpath=[]
simple_hill_climb(root)
for i in goalpath:
    i.display()

print('Success!')