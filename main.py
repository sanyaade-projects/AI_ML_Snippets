import random

board = [2,2,2,2,2,2,2,2,2]
players=['C','H']

def Go(n):
    if board[n]==2:
        board[n]=5

def PossWin(P):
    for i in range(3):                  #rows
        ans=1
        for j in range(3):
            ans*=board[3*i+j]
            if board[3*i+j]==2:
                cell=3*i+j
    if P=='X' and ans==18:
        return cell
    if P=='O' and ans==50:
        return cell
    for i in range(3):                  #cols
        ans=1
        for j in range(3):
            ans*=board[i+3*j]
            if board[i+3*j]==2:
                cell=i+3*j
    if P=='X' and ans==18:
        return cell
    if P=='O' and ans==50:
        return cell
    ans=board[0]*board[4]*board[8]
    if board[0]==2: cell=0
    if board[4]==2: cell=4
    if board[8]==2: cell=8
    if P=='X' and ans==18:
        return cell
    if P=='O' and ans==50:
        return cell
    ans=board[2]*board[4]*board[6]
    if board[2]==2: cell=2
    if board[4]==2: cell=4
    if board[6]==2: cell=6
    if P=='X' and ans==18:
        return cell
    if P=='O' and ans==50:
        return cell

def display():
    for i in range(0,7,3):
        print('\t',board[i],' | ',board[i+1],' | ',board[i+2])

def check(P):
    for i in range(3):                  #rows
        ans=1
        for j in range(3):
            ans*=board[3*i+j]
            if board[3*i+j]==2:
                cell=3*i+j
    if ans==27:
        return cell
    if P=='O' and ans==50:
        return cell
    for i in range(3):                  #cols
        ans=1
        for j in range(3):
            ans*=board[i+3*j]
            if board[i+3*j]==2:
                cell=i+3*j
    if P=='X' and ans==18:
        return cell
    if P=='O' and ans==50:
        return cell
    ans=board[0]*board[4]*board[8]
    if board[0]==2: cell=0
    if board[4]==2: cell=4
    if board[8]==2: cell=8
    if P=='X' and ans==18:
        return cell
    if P=='O' and ans==50:
        return cell
    ans=board[2]*board[4]*board[6]
    if board[2]==2: cell=2
    if board[4]==2: cell=4
    if board[6]==2: cell=6
    if P=='X' and ans==18:
        return cell
    if P=='O' and ans==50:
        return cell

def turn(P):
    if P=='X':
        t=int(input("Please select a position to play (0-8):"))
        board[t]=3
        display()
        check('X')
        return turn('O')
    else:
        cell = PossWin('O')
        if cell==None:
            if PossWin('X')!=None:
                Go(PossWin('X'))
            elif board[4]==2:
                Go(4)
            elif board[0]==2:
                Go(0)
            elif board[2]==2:
                Go(2)
            elif board[6]==2:
                Go(6)
            elif board[8]==2:
                Go(8)
            else:
                while True:
                    r=random.choice(range(9))
                    if board[r]!=2:
                        Go(r)
                        break
        else:
            Go(cell)
            print('I won!!!')
            display()
            return
        print("My chance:")
        display()
        return turn('X')

def main():
    if random.choice([1,0]) == 0:
        turn('O')
    else:
        turn('X')

display()
main()