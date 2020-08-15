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

theBoard = [' '] * 10

getXMove(theBoard)
drawBoard(theBoard)
getOMove(theBoard)
drawBoard(theBoard)
getXMove(theBoard)
drawBoard(theBoard)
getOMove(theBoard)
drawBoard(theBoard)
getXMove(theBoard)
drawBoard(theBoard)
getOMove(theBoard)
drawBoard(theBoard)
getXMove(theBoard)
drawBoard(theBoard)
getOMove(theBoard)
drawBoard(theBoard)
getXMove(theBoard)
drawBoard(theBoard)

#這樣寫很醜...
#而且思考看看，這樣寫還有什麼問題
#我這次想嘗試加入，決定由O還是X開始