def drawBoard(board):
	# This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def getXMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    move = int(move)
    board[move] = 'X'

def getOMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    move = int(move)
    board[move] = 'O'

def whoGoesFirst():
    who = ''
    while not (who == 'O' or who == 'X'):
        who = input('Who goes first?')
    return who

def isWinner(board, turn):
    # Given a board and a player's letter, this function returns True if that player has won.
    return ((board[7] == turn and board[8] == turn and board[9] == turn) or # across the top
    (board[4] == turn and board[5] == turn and board[6] == turn) or # across the middle
    (board[1] == turn and board[2] == turn and board[3] == turn) or # across the bottom
    (board[7] == turn and board[4] == turn and board[1] == turn) or # down the left side
    (board[8] == turn and board[5] == turn and board[2] == turn) or # down the middle
    (board[9] == turn and board[6] == turn and board[3] == turn) or # down the right side
    (board[7] == turn and board[5] == turn and board[3] == turn) or # diagonal
    (board[9] == turn and board[5] == turn and board[1] == turn)) # diagonal

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print('Welcome to Tic Tac Toe!')
# Reset the board
theBoard = [' '] * 10
turn = whoGoesFirst()
print('The ' + turn + ' will go first.')
gameIsPlaying = True

while gameIsPlaying:
        if turn == 'X':
            # X's turn.
            drawBoard(theBoard)
            getXMove(theBoard)
            if isWinner(theBoard, turn):
                drawBoard(theBoard)
                print('Hooray!' + turn + ' have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'O'

        else:
            # O's turn.
            drawBoard(theBoard)
            getOMove(theBoard)
            if isWinner(theBoard, turn):
                drawBoard(theBoard)
                print('Hooray!' + turn + ' have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'X'