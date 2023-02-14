from itertools import combinations

board = [0,0,0,0,0,0,0,0,0]
ref=[7,2,3,0,4,8,5,6,1]
human = 'X'
computer = 'O'

def turn(P,step):
    #print(board)
    if step==9:
        h=PossWin(human)
        c=PossWin(computer)
        if len(h)!=0 and P=='H':
            print('Congratulations! You won!!!')
            return
        elif len(c)!=0 and P=='C':
            print('I won!!!')
            return
        else:
            print('Tie!')
            return
    arr = PossWin(human)
    if P=='H':
        while True:
            t = int(input("Please select a position to play (1-9):"))
            x=ref[t-1]
            if board[x]==0:
                break
        board[x]=human
        display(step)
        if x in arr:
            print('Congratulations! You won!!!')
            return
        print('End of step',step)
        return turn('C',step+1)
    else:
        l = PossWin(computer)
        if len(l)!=0:
            board[l[0]]=computer
            display(step)
            print('I won!')
            return
        if len(arr)!=0:
            board[arr[0]]=computer
            display(step)
            return turn('H',step+1)
        if board[4]==0:
            board[4]=computer
            display(step)
            return turn('H',step+1)
        if board[7]==0:
            board[7]=computer
            display(step)
            return turn('H',step+1)
        if board[3]==0:
            board[3]=computer
            display(step)
            return turn('H',step+1)
        if board[1]==0:
            board[1]=computer
            display(step)
            return turn('H',step+1)
        if board[5]==0:
            board[5]=computer
            display(step)
            return turn('H',step+1)

def PossWin(player):
    prop=[]
    winplaces=[]
    for i in range(9):
        if board[i]==player:
            prop.append(i+1)
    if len(prop)!=0:
        for i in combinations(prop, 2):
            S=i[0]+i[1]
            D=15-S
            if D>0 and D<10 and board[D-1]==0:
                winplaces.append(D-1)
    return winplaces

def Go(n):
    board[n-1]=computer

def display(step):
    print('Step :',step)
    print('\t',board[7],'|',board[2],'|',board[3])
    print('\t',board[0],'|',board[4],'|',board[8])
    print('\t',board[5],'|',board[6],'|',board[1])

#toss and decide who plays first
#player to play first gets 'x'
#turn(human,1)
display(0)
if human=='X':
    turn('H',1)
else:
    turn('C',1)