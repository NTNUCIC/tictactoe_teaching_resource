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

input('觀察一下，我要講解陣列哩')
input('啊，還有def')
input('嗯...先講function好了')

move = input("Make a move: ")
input('這邊會出錯，要修改才能執行')
theBoard[move] = 'O'
drawBoard(theBoard)