board = ['1','2','3','4','5','6','7','8','X']
pos=8

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
    else:
        pass
    if mov == 2 and not (pos > 5):
        board[pos],board[pos+3] = board[pos+3],board[pos]
        pos+=3
        display()
    else:
        pass
    if mov == 4 and not (pos%3 == 0):
        board[pos],board[pos-1] = board[pos-1],board[pos]
        pos-=1
        display()
    else:
        pass
    if mov == 6 and not (pos%3 == 2):
        board[pos],board[pos+1] = board[pos+1],board[pos]
        pos+=1
        display()
    else:
        pass

def main():
    print('Moves:\n8: Up\n4: Left\n6: Right\n2: Down')
    display()
    while True:
        x=int(input('Move:'))
        move(x)
        if x==0:
            break

main()