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



drawBoard(theBoard)

input('第一討論')
#棋下去的時候，要注意什麼？輸入值要注意什麼？

move = input('Make a move: ')
move = int(move)
theBoard[move] = 'O'
drawBoard(theBoard)

#輸入1~9試試看，發現了什麼？

#輸入英文字母看看，發現了什麼？

input('第二討論')
theBoard = [' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
drawBoard(theBoard)

move = input('Make a move: (輸入1看看)')
move = int(move)
theBoard[move] = 'X'
drawBoard(theBoard)


