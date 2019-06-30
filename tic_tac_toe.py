#let's go

def game_start():
    print('                  Tic Tac Toe')
    print('                  By Ying Ma')

def display_board(board):
    print ('                         '+board[7]+'|'+board[8]+'|'+board[9])
    print ('                         '+board[4]+'|'+board[5]+'|'+board[6])
    print ('                         '+board[1]+'|'+board[2]+'|'+board[3])
    
def clear_board():
    print('\n'*100)
    
def clear_screen():
    print('\n'*100)
    
def choose_side():
    side = input('Player 1, would you like to play as "X" or as "O"?\n')
    i=0
    while side!="X" and side!="O" and i<2:
        side = input('Let\'s try again! Please input "X" or "O":\n')
        i+=1
    if i==2:
        print('Okay, you will play as "O"')
        side="O"
    return side

def check_board_empty(marker):
    return board[marker]==' '

def place_marker():
    global marker
    global side
    
    marker = ' '
    
    try:
        marker=int(input(f'User {side}, Please put down a marker, use num key as position reference, input 1-9:\n'))
    except:
        print("That's not a integer!")
        
    while marker not in range(1,10) or not isinstance(marker,int):
        try:
            marker=int(input('Please enter (1-9) only:\n'))
        except:
            marker="wrong"
          
    if check_board_empty(marker):
        if side=='O':
            board[marker]=side
        elif side=='X':
            board[marker]=side
    else:
        while not check_board_empty(marker):
            marker=int(input('Sorry, this position is taken, please put it somewhere else:\n'))
        if side=='O':
            board[marker]=side
        elif side=='X':
            board[marker]=side
        
def switch_side():
    global side
    if side=='O':
        side='X'
    else:
        side='O'

def win_check():
    return ((board[7] ==  board[8] ==  board[9]==side) or (board[4] ==  board[5] ==  board[6]==side) or (board[1] ==  board[2] ==  board[3]==side) or \
    (board[7] ==  board[4] ==  board[1]==side) or \
    (board[8] ==  board[5] ==  board[2]==side) or \
    (board[9] ==  board[6] ==  board[3]==side) or \
    (board[7] ==  board[5] ==  board[3]==side) or \
    (board[9] ==  board[5] ==  board[1]==side))
    
def game():
    global board, counter, side
    
    board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    counter = 0

    side = choose_side()
    display_board(board)
    counter =  0

    while counter<9 and not win_check():

        place_marker()
        display_board(board)
        counter +=1
        if win_check():
            break
        switch_side()
    
    
    if counter==9:
        print('            Draw!')
    elif win_check():
            print(f'      Player {side} won!')

restart=True
while restart == True:
    game_start()
    game()
    restart=input('Would you like to play again? (Y/N):\n')
    restart=(restart=='Y')
    if restart:
        clear_screen()
    else:
        print ('               Thanks for playing!')
        break