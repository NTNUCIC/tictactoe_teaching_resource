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

        turn = 'O'

    else:
        # O's turn.
        drawBoard(theBoard)
        getOMove(theBoard)

        turn = 'X'

"""
還有辦法更好嗎？
下到一半有人贏了，還要繼續下嗎？
下到九格都滿了，還要繼續下嗎？
"""

"""

！！！初始化棋盤！！！

while 遊戲正在進行：
    if 玩家1的回合：
        玩家1下棋
        if 玩家1勝利：
            遊戲結束
        else：
            if 棋盤下滿了：
                遊戲結束
            else：
                換玩家2的回合
    else：
        玩家2下棋
        if 玩家2勝利：
            遊戲結束
        else：
            if 棋盤下滿了：
                遊戲結束
            else：
                換玩家1的回合

"""