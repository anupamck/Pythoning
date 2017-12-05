import random 

theBoard = {'tl':' ','tm':' ','tr':' ',         #Define new board
            'ml':' ','mm':' ','mr':' ',
            'bl':' ','bm':' ','br':' ',}

def clearBoard(board):                           #Clear board before game start
    global theBoard
    theBoard = {'tl':' ','tm':' ','tr':' ',     
            'ml':' ','mm':' ','mr':' ',
            'bl':' ','bm':' ','br':' ',}

   
def printBoard(board):                           #Print current board status
    print(board['tl'] + '|' + board['tm'] + '|' + board['tr'])
    print('-+-+-')
    print(board['ml'] + '|' + board['mm'] + '|' + board['mr'])
    print('-+-+-')
    print(board['bl'] + '|' + board['bm'] + '|' + board['br'])


def winBoard(char):                                                                                #Check if game is over
    
    return((theBoard['tl'] == char and theBoard['tm'] == char and theBoard['tr'] == char) or       #Top row
            (theBoard['ml'] == char and theBoard['mm'] == char and theBoard['mr'] == char) or      #Middle row
           (theBoard['bl'] == char and theBoard['bm'] == char and theBoard['br'] == char) or       #Bottom row
           (theBoard['tl'] == char and theBoard['ml'] == char and theBoard['bl'] == char) or       #Left column
           (theBoard['tm'] == char and theBoard['mm'] == char and theBoard['bm'] == char) or       #Middle column
           (theBoard['tr'] == char and theBoard['mr'] == char and theBoard['br'] == char) or       #Right column
           (theBoard['tl'] == char and theBoard['mm'] == char and theBoard['br'] == char) or       #Downward diagonal
            (theBoard['tr'] == char and theBoard['mm'] == char and theBoard['bl'] == char))        #Upward diagonal

def fullBoard():
    return(theBoard['tl'] != ' ' and theBoard['tm'] != ' ' and theBoard['tr'] != ' '               #Check if game is a draw
           and theBoard['ml'] != ' ' and theBoard['mm'] != ' ' and theBoard['mr'] != ' '           #All slots in board are non empty
           and theBoard['bl'] != ' ' and theBoard['bm'] != ' ' and theBoard['br'] != ' ')

winJ = ' '                                                                                          #Define and initialize near-win varaible

lossJ = ' '                                                                                         #Define and initialize near-loss varaible        

def nearWin():                                                                                      #Return position of near-win with winJ variable
    global winJ                                                                                     
    if (theBoard['tl'] + theBoard['tm'].strip() + theBoard['tr']).strip() == 'OO':                  #Top row
         winJ = 't,x' 
    elif (theBoard['ml'] + theBoard['mm'].strip() + theBoard['mr']).strip() == 'OO':                #Middle row
         winJ = 'm,x'
    elif (theBoard['bl'] + theBoard['bm'].strip() + theBoard['br']).strip() == 'OO':                #Bottom row
         winJ = 'b,x' 
    elif (theBoard['tl'] + theBoard['ml'].strip() + theBoard['bl']).strip() == 'OO':                #Left column
         winJ = 'x,l'                                                                               
    elif (theBoard['tm'] + theBoard['mm'].strip() + theBoard['bm']).strip() == 'OO':                #Middle column
         winJ = 'x,m' 
    elif (theBoard['tr'] + theBoard['mr'].strip() + theBoard['br']).strip() == 'OO':                #Right column
         winJ = 'x,r' 
    elif (theBoard['tl'] + theBoard['mm'].strip() + theBoard['br']).strip() == 'OO':                #Downward diagonal
         winJ = 'd1'
    elif (theBoard['tr'] + theBoard['mm'].strip() + theBoard['bl']).strip() == 'OO':                #Upward diagonal
         winJ = 'd2'

def nearLoss():
    global lossJ
    if (theBoard['tl'] + theBoard['tm'].strip() + theBoard['tr']).strip() == 'XX':                  #Similar to above for near-loss, with lossJ variable
         lossJ = 't,x' 
    elif (theBoard['ml'] + theBoard['mm'].strip() + theBoard['mr']).strip() == 'XX':
         lossJ = 'm,x'
    elif (theBoard['bl'] + theBoard['bm'].strip() + theBoard['br']).strip() == 'XX':
         lossJ = 'b,x' 
    elif (theBoard['tl'] + theBoard['ml'].strip() + theBoard['bl']).strip() == 'XX':
         lossJ = 'x,l' 
    elif (theBoard['tm'] + theBoard['mm'].strip() + theBoard['bm']).strip() == 'XX':
         lossJ = 'x,m' 
    elif (theBoard['tr'] + theBoard['mr'].strip() + theBoard['br']).strip() == 'XX':
         lossJ = 'x,r' 
    elif (theBoard['tl'] + theBoard['mm'].strip() + theBoard['br']).strip() == 'XX':
         lossJ = 'd1'
    elif (theBoard['tr'] + theBoard['mm'].strip() + theBoard['bl']).strip() == 'XX':
         lossJ = 'd2'
        
print("Welcome, friend, to noob tic-tac-toe")

playAgain = True

while playAgain:                                                                                    #Outermost loop - if play again is True

    d=0
    
    while d ==0:                                                                                    #While to check for correct difficulty level entry
        print("Choose your diffficulty level (Feeling lucky?) \nType in easy or hard")
        difficulty = input().lower().strip()
        if difficulty not in ['easy', 'hard']:
            print("Type in either 'easy' or 'hard'... please. My vocabulary isn't as colourful as yours")
        else:
            d+=1

    player = random.choice(['human','computer'])                                                    #Select who goes first randomly
   
    if player == 'computer':
        print("The computer will play first")
    else:
        printBoard(theBoard)

    i = 0    
    turnCount = 0                                                                                   #Turn counter is reset (for use in logic)
      
    for i in range (0,193):                                                                         #for with a very large index. for is used because loop can be borken in case game is over anytime

        if player == 'human':                                                                       #Start only if player is human
        
            t=0                                                                                     #Logic to ensure that top-left is same as left-top and so on
            while t == 0:
                print("Play your turn. E.g. bm for bottom-middle")
                turn = input().lower().strip()
                if turn == 'lt':
                    turn = 'tl'                    
                elif turn == 'mt':
                     turn = 'tm'
                elif turn == 'rt':
                    turn = 'tr'
                elif turn == 'lm':
                    turn = 'ml'
                elif turn == 'rm':
                    turn = 'mr'
                elif turn == 'lb':
                    turn = 'bl'
                elif turn == 'mb':
                    turn = 'bm'
                elif turn == 'rb':
                    turn = 'br'    
                                   
                if turn not in ['tl', 'tm', 'tr', 'ml', 'mm', 'mr', 'bl', 'bm', 'br']:              #Error checks to see if valid move is made
                    print("Enter a valid move")
                elif theBoard[turn] != ' ':
                    print("Choose an empty space")
                else: t+=1
                
            theBoard[turn] = 'X'                                                                    #Update player's move

            if winBoard('X'):                                                                       #Check if move end's game with win
                printBoard(theBoard)
                print("Congratulations! You win")
                break
            elif fullBoard():                                                                       #Check if move end's game with win
                printBoard(theBoard)
                print("A shake of the hands. It's a draw")                    
                break

        if player == 'human' or player == 'computer':

            nearWin()                                                                               #Check if win is possible with next move 

            nearLoss()                                                                              #Check if urgent defence is needed in the next move

            #print('winJ = ' + winJ)

            #print('lossJ = ' + lossJ)
            
            nWLogic = winJ.split(",")                                                               #Logic to detect where the win or loss is occuring, to be used later

            nLLogic = lossJ.split(",")
                                  
            if winJ == ' ':                                                                         #Check if there is no ready win or ready loss with the next move (win has higher priority and is the outer loop)
                if lossJ == ' ':                                                                    #Defence loop begins
                    if difficulty == 'easy':                                                        #Make random move in any available whitespace on board. Keep looping until whitespace is found
                        k = 0
                        while k == 0:
                            compMove = random.choice(['t','m','b'])+random.choice(['l','m','r'])
                            if theBoard[compMove] == ' ':
                                theBoard[compMove] = 'O'
                                k+=1
                            
                    elif difficulty == 'hard':                                                      #For 1st two moves (crucial to determine result), take center position if not yet taken
                        if turnCount in [0,1]:                                
                            if theBoard['mm'] == ' ':
                                theBoard['mm'] = 'O'
                                turnCount+=1
                                #print(turnCount)
                                
                            else:                                    
                                if theBoard['mm'] == 'O':                                           #Logic to avoid losses                                            
                                    if theBoard['mr'] == 'X':
                                        k = 0
                                        while k == 0:
                                            compMove = random.choice(['b','t'])+'r'
                                            if theBoard[compMove] == ' ':
                                                theBoard[compMove] = 'O'
                                                k+=1
                                                turnCount+=1
                                                #print(turnCount)

                                    elif theBoard['bm'] == 'X':                                     #Logic to avoid losses
                                        k = 0
                                        while k == 0:
                                            compMove = 'b' + random.choice(['l','r'])
                                            if theBoard[compMove] == ' ':
                                                theBoard[compMove] = 'O'
                                                k+=1
                                                turnCount+=1
                                                #print(turnCount)

                                    elif theBoard['ml'] == 'X':                                     #Logic to avoid losses
                                        k = 0
                                        while k == 0:
                                            compMove = random.choice(['t','b']) + 'l'
                                            if theBoard[compMove] == ' ':
                                                theBoard[compMove] = 'O'
                                                k+=1
                                                turnCount+=1
                                                #print(turnCount)

                                    elif theBoard['tm'] == 'X':                                     #Logic to avoid losses
                                        k = 0
                                        while k == 0:
                                            compMove = 't' + random.choice(['l','r'])
                                            if theBoard[compMove] == ' ':
                                                theBoard[compMove] = 'O'
                                                k+=1
                                                turnCount+=1
                                                #print(turnCount)
                                    
                                    else: 
                                        k = 0                                                       #Logic to avoid losses
                                        while k == 0:
                                            compMove = random.choice([random.choice(['t','b']) + 'm', 'm' + random.choice(['l','r'])])
                                            if theBoard[compMove] == ' ':
                                                theBoard[compMove] = 'O'
                                                k+=1
                                                turnCount+=1
                                                #print(turnCount)


                                else:
                                    k = 0
                                    while k == 0:                                                   #Show preference for corner slots if no loss threatened
                                        compMove = random.choice(['t','b'])+random.choice(['l','r'])
                                        if theBoard[compMove] == ' ':
                                            theBoard[compMove] = 'O'
                                            k+=1
                                            turnCount+=1
                                            #print(turnCount)
                                            
                        else:
                                k = 0
                                while k == 0:                                                       #After 1st two moves, provided obvious danger is avoided, play completely random move
                                    compMove = random.choice(['t','m','b'])+random.choice(['l','m','r'])
                                    if theBoard[compMove] == ' ':
                                        theBoard[compMove] = 'O'
                                        k+=1
                                        turnCount+=1
                                        #print(turnCount)
                                        
                elif nLLogic[0] == 'x':                                                             #Defend imminent threat based on feedback from nearLoss()
                    k = 0
                    while k < 3:
                        compMove = ['t','m','b'][k] + nLLogic[1]
                        if theBoard[compMove] == ' ':
                            theBoard[compMove] = 'O'
                        k+=1
                        lossJ = ' '                                                                 #Reset lossJ after mitigating threat    

                elif nLLogic[0] == 'd1':                                                            #Defend imminent threat based on feedback from nearLoss()
                    k = 0
                    while k < 3:
                        compMove = ['tl','mm','br'][k]
                        if theBoard[compMove] == ' ':
                            theBoard[compMove] = 'O'
                        k+=1
                        lossJ = ' '                                                                 #Reset lossJ after mitigating threat  
             
                elif nLLogic[0] == 'd2':                                                            #Same as comments above
                    k = 0
                    while k < 3:
                        compMove = ['tr','mm','bl'][k]
                        if theBoard[compMove] == ' ':
                            theBoard[compMove] = 'O'
                        k+=1
                        lossJ = ' '

                elif nLLogic[1] == 'x':                                                             #Same as comments above; defence loop ends
                    k = 0
                    while k < 3:
                        compMove = nLLogic[0]+['l','m','r'][k]
                        if theBoard[compMove] == ' ':
                            theBoard[compMove] = 'O'
                        k+=1
                        lossJ = ' '
                        
            elif nWLogic[0] == 'x':                                                                 #Check if win possible with next move; attack loop continues                                    
                k = 0
                while k < 3:
                    compMove = ['t','m','b'][k] + nWLogic[1]
                    if theBoard[compMove] == ' ':
                        theBoard[compMove] = 'O'
                    k+=1
                    winJ = ' '                                                                      #Reset winJ for next game  
                   
            elif nWLogic[0] == 'd1':
                k = 0
                while k < 3:
                    compMove = ['tl','mm','br'][k]                  
                    if theBoard[compMove] == ' ':
                        theBoard[compMove] = 'O'
                    k+=1
                    winJ = ' '
             
            elif nWLogic[0] == 'd2':                                                                #Same comments as above
                k = 0
                while k < 3:
                    compMove = ['tr','mm','bl'][k]
                    if theBoard[compMove] == ' ':
                        theBoard[compMove] = 'O'
                    k+=1
                    winJ = ' '
                        
            elif nWLogic[1] == 'x':                                                                 #Same comments as above
                k = 0
                while k < 3:
                    compMove = nWLogic[0]+['l','m','r'][k]
                    if theBoard[compMove] == ' ':
                        theBoard[compMove] = 'O'
                    k+=1
                    winJ = ' '

            if winBoard('O'):                                                                       #Detect if computer's moves ends game
                printBoard(theBoard)
                print("Sorry. You lose!")                    
                break
             
            elif fullBoard():
                printBoard(theBoard)
                print("A shake of the hands. It's a draw")
                break

            player = 'human'
            
            printBoard(theBoard)

    inputWhile = 0                                                                                  #While loop for user input sanity check
    while inputWhile == 0:
        print("Play again? - Type in 'Y' or 'N'")
        userInput = input().lower()
        #turnLoop = 0
        if userInput == 'n':
            playAgain = False
            inputWhile+=1
        if userInput == 'y':
            playAgain = True                                                                        #Play Again = True starts the master While loop again
            clearBoard(theBoard)                                                                    #Clear board for new game
            inputWhile+=1
        elif userInput not in ['n', 'y']:
            print ("Invalid input. Please enter either 'Y' or 'N'... only. I'm a dumb computer, yo!")
        
