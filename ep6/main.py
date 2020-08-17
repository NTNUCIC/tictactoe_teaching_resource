from random import randint as rand

"""
	newBoard - return a new board object.

	The board is declare as an list 10 of string.
	Take the board[0] as the game state info.
"""
def newBoard():
	board = list(' '*10)
	return board


"""
	drawBoard - prints out the board that it was passed.
	@board: list 10 of string.

	The board is displayed like the right panel on the keyboard
"""
def drawBoaard(board):
	print(' {} | {} | {} '.format(board[7], board[8], board[9]))
	print('---+---+---')
	print(' {} | {} | {} '.format(board[4], board[5], board[6]))
	print('---+---+---')
	print(' {} | {} | {} '.format(board[1], board[2], board[3]))


"""
	isFree - return True if the place is free on the board.
	@board: list 10 of string.
	@place: integer in range(1, 9).
"""
def isFree(board, place):
	return place in range(1, 9+1) and board[place] == ' '


"""
	takeMove - place a chess on the board.
	@board: list 10 of string.
	@place: integer in range(1, 9).
	@chess: string

	Return False if the place on the board is already have chest.
"""
def takeMove(board, place, chess):
	if isFree(board, place):
		board[place] = chess
		return True
	else:
		return False


"""
	Move - ask the user where he wants to play chess.
	@board: list 10 of string.
	@chess: string
"""
def Move(board, chess):
	print("Where to play chess? [1-9] ")
	place = int(input())
	while not (place in range(1, 9+1) and takeMove(board, place, chess)):
		print("The input is illegal, place try again.")
		place = int(input())


"""
	updateState - update the game state of player wining.
	@board: list 10 of string.

	store the result in the board[0].
"""
def updateState(board):
	def theSame(a, b, c):
		return a == b and b == c and a + b + c != '   '
	# check if the player has won the game.
	## raw
	if theSame(board[1], board[2], board[3]): board[0] = board[1]
	elif theSame(board[4], board[5], board[6]): board[0] = board[4]
	elif theSame(board[7], board[8], board[9]): board[0] = board[7]
	## column
	elif theSame(board[1], board[4], board[7]): board[0] = board[1]
	elif theSame(board[2], board[5], board[8]): board[0] = board[2]
	elif theSame(board[3], board[6], board[9]): board[0] = board[3]
	## diagonal
	elif theSame(board[1], board[5], board[9]): board[0] = board[1]
	elif theSame(board[3], board[5], board[7]): board[0] = board[3]


"""
	haveWinner - return True if any player has won the game.
	@board: list 10 of string.
"""
def haveWinner(board):
	return (board[0] != ' ')


""" Main function start here. """

board = newBoard()
chessSet = ['O', 'X']
turns = 0

print('Welcome to Tic-Tac-Toe.')
print("Which chess did you like? [O/X]")

player_chess = input()
while player_chess not in chessSet:
	print("The input is illegal, place try again.")
	player_chess = input()

chessSet.remove(player_chess)
computer_chess = chessSet[0]

while turns < 9:
	# player
	drawBoaard(board)
	Move(board, player_chess)
	updateState(board)
	if haveWinner(board):
		print('player {}, have won the game.'.format(player_chess)); break
	else:
		turns += 1

	# computer
	tryplace = rand(1, 9)
	while not takeMove(board, tryplace, computer_chess):
		tryplace = rand(1, 9)
	updateState(board)
	
	if haveWinner(board):
		print('player {}, have won the game.'.format(player_chess)); break
	else:
		turns += 1
else:
    print('The game is a tie!')

input()