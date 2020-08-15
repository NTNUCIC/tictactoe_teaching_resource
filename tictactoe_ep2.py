theBoard = [' '] * 10

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

input('這邊教一下while loop')
input('還有if-else')
input('教得很淺啦...熟python的就聽聽吧')
input('但也因為很簡單，所以初學者還是要記得多鑽研')

input('教之前，我們來觀察一下以下的程式')

drawBoard(theBoard)

#---------------------------------

input('第一手')
move = input('Make a move: ')
move = int(move)
theBoard[move] = 'O'
drawBoard(theBoard)

#---------------------------------

input('第二手')
move = input('Make a move: ')
move = int(move)
theBoard[move] = 'X'
drawBoard(theBoard)

#---------------------------------

input('第三手')
move = input('Make a move: ')
move = int(move)
theBoard[move] = 'O'
drawBoard(theBoard)

#---------------------------------

input('第四手')
move = input('Make a move: ')
move = int(move)
theBoard[move] = 'X'
drawBoard(theBoard)

#---------------------------------

input('第五手')
move = input('Make a move: ')
move = int(move)
theBoard[move] = 'O'
drawBoard(theBoard)

#---------------------------------

input('第六手')
move = input('Make a move: ')
move = int(move)
theBoard[move] = 'X'
drawBoard(theBoard)

#---------------------------------

input('第七手')
move = input('Make a move: ')
move = int(move)
theBoard[move] = 'O'
drawBoard(theBoard)

#---------------------------------

input('第八手')
move = input('Make a move: ')
move = int(move)
theBoard[move] = 'X'
drawBoard(theBoard)

#---------------------------------

input('第九手')
move = input('Make a move: ')
move = int(move)
theBoard[move] = 'O'
drawBoard(theBoard)


"""
思考這支程式有什麼問題？

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