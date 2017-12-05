theBoard = {'tl':' ','tm':' ','tr':' ',     #New board is defined and refreshed at the start
            'ml':' ','mm':' ','mr':' ',
            'bl':' ','bm':' ','br':' ',}

import random 

def printBoard(board):                      #Function for printing the current state of the board
    print(board['tl'] + '|' + board['tm'] + '|' + board['tr'])
    print('-+-+-')
    print(board['ml'] + '|' + board['mm'] + '|' + board['mr'])
    print('-+-+-')
    print(board['bl'] + '|' + board['bm'] + '|' + board['br'])
printBoard(theBoard)

def winBoard(char):
    return((theBoard['tl'] == char and theBoard['tm'] == char and theBoard['tr'] == char) or       #Top row
            (theBoard['ml'] == char and theBoard['mm'] == char and theBoard['mr'] == char) or      #Middle row
           (theBoard['bl'] == char and theBoard['bm'] == char and theBoard['br'] == char) or       #Bottom row
           (theBoard['tl'] == char and theBoard['ml'] == char and theBoard['bl'] == char) or       #Left column
           (theBoard['tm'] == char and theBoard['mm'] == char and theBoard['bm'] == char) or       #Middle column
           (theBoard['tr'] == char and theBoard['mr'] == char and theBoard['br'] == char) or       #Right column
           (theBoard['tl'] == char and theBoard['mm'] == char and theBoard['br'] == char) or       #Downward diagonal
            (theBoard['tr'] == char and theBoard['mm'] == char and theBoard['bl'] == char))        #Upward diagonal

def fullBoard():
    return(theBoard['tl'] != ' ' and theBoard['tm'] != ' ' and theBoard['tr'] != ' '               #All slots in board are non empty
           and theBoard['ml'] != ' ' and theBoard['mm'] != ' ' and theBoard['mr'] != ' '
           and theBoard['bl'] != ' ' and theBoard['bm'] != ' ' and theBoard['br'] != ' ')

i = 0

for i in (0,5):
    
    t=0                                                                                             #Detect invalid moves
    while t == 0:
        print("Play your turn. E.g. bm for bottom-middle")
        turn = input()
        if turn not in ['tl', 'tm', 'tr', 'ml', 'mm', 'mr', 'bl', 'bm', 'br']:
            print("Enter a valid move")
        elif theBoard[turn] != ' ':
            print("Choose an empty space")
        else: t+=1
        
    theBoard[turn] = 'X'

    if winBoard('X'):
        printBoard(theBoard)
        print("Congratulations! You win")
        break
    elif fullBoard():
        printBoard(theBoard)
        print("Well played. It's a draw")
        break

    k = 0
    while k == 0:
        compMove = random.choice(['t','m','b'])+random.choice(['l','m','r'])
        if theBoard[compMove] == ' ':
            theBoard[compMove] = 'O'
            k+=1

    printBoard(theBoard)

    if winBoard('O'):
        print("Sorry. You lose!")
        break
    elif fullBoard():
        print("Well played. It's a draw")
        break

text = '''
for x in range(0,5):
    print("Play your turn. E.g. bm")
    turn = input()
    theBoard[turn] = 'X'
    if theBoard['tl'] == 'X' and theBoard['tm'] == 'X' and theBoard['tr'] == 'X':
        printBoard(theBoard)
        print("Congratulations! You win")
        break
    elif theBoard['ml'] == 'X' and theBoard['mm'] == 'X' and theBoard['mr'] == 'X':
        printBoard(theBoard)
        print("Congratulations! You win")
        break
    elif theBoard['bl'] == 'X' and theBoard['bm'] == 'X' and theBoard['br'] == 'X':
        printBoard(theBoard)
        print("Congratulations! You win")
        break
    elif theBoard['tl'] == 'X' and theBoard['ml'] == 'X' and theBoard['bl'] == 'X':
        printBoard(theBoard)
        print("Congratulations! You win")
        break
    elif theBoard['tm'] == 'X' and theBoard['mm'] == 'X' and theBoard['bm'] == 'X':
        printBoard(theBoard)
        print("Congratulations! You win")
        break
    elif theBoard['tr'] == 'X' and theBoard['mr'] == 'X' and theBoard['br'] == 'X':
        printBoard(theBoard)
        print("Congratulations! You win")
        break
    elif theBoard['tl'] == 'X' and theBoard['mm'] == 'X' and theBoard['br'] == 'X':
        printBoard(theBoard)
        print("Congratulations! You win")
        break
    elif theBoard['tr'] == 'X' and theBoard['mm'] == 'X' and theBoard['bl'] == 'X':     
        printBoard(theBoard)
        print("Congratulations! You win")
        break

    for x in range (0,4):
        comp = random.choice(['t','m','b'])+random.choice(['l','m','r'])
        if theBoard[comp] == ' ':
            theBoard[comp] = 'O'
            break
    printBoard(theBoard)
    if theBoard['tl'] == 'O' and theBoard['tm'] == 'O' and theBoard['tr'] == 'O':
        print("Sorry, you lose!")
        break
    elif theBoard['ml'] == 'O' and theBoard['mm'] == 'O' and theBoard['mr'] == 'O':
        print("Sorry, you lose!")
        break
    elif theBoard['bl'] == 'O' and theBoard['bm'] == 'O' and theBoard['br'] == 'O':
        print("Sorry, you lose!")
        break
    elif theBoard['tl'] == 'O' and theBoard['ml'] == 'O' and theBoard['bl'] == 'O':
        print("Sorry, you lose!")
        break
    elif theBoard['tm'] == 'O' and theBoard['mm'] == 'O' and theBoard['bm'] == 'O':
        print("Sorry, you lose!")
        break
    elif theBoard['tr'] == 'O' and theBoard['mr'] == 'O' and theBoard['br'] == 'O':
        print("Sorry, you lose!")
        break
    elif theBoard['tl'] == 'O' and theBoard['mm'] == 'O' and theBoard['br'] == 'O':
        print("Sorry, you lose!")
        break
    elif theBoard['tr'] == 'O' and theBoard['mm'] == 'O' and theBoard['bl'] == 'O':
        print("Sorry, you lose!")
        break
    elif theBoard['tl'] != ' ' and theBoard['tm'] != ' ' and theBoard['tr'] != ' ' and theBoard['ml'] != ' ' and theBoard['mm'] != ' ' and theBoard['mr'] != ' ' and theBoard['bl'] != ' ' and theBoard['bm'] != ' ' and theBoard['br'] != ' ':
        print("It's a draw. Well played")    
    '''
