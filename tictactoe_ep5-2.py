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

theBoard = [' ', 'X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
drawBoard(theBoard)

print(theBoard[9] == 'X' and theBoard[5] == 'X' and theBoard[1] == 'X')

#寫一個函式，判斷誰是勝利者，應該考慮什麼input？


