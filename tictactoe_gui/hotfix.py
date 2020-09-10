from copy import deepcopy
import pygame as pg
from random import randint as rand
from time import sleep

"""
	init - return a new board object.

	The board is declare as an list 10 of string.
	Take the board[0] as the game state info.
"""
def init():
	pg.init()
	pg.display.set_caption('tictactoe_v1.1')
	screen = pg.display.set_mode((400, 600))
	screen.fill((255, 255, 255))
	bg = pg.image.load('tictactoe_1.jpg')
	screen.blit(bg, [0, 0])
	pg.display.update()
	board = [['', '', ''], ['', '', ''], ['', '', '']]
	return screen, board


"""
	drawBoard - prints out the board that it was passed.
	@board: list 10 of string.

	The board is displayed like the right panel on the keyboard
"""
def drawBoaard(screen, board):
	for x in range(3):
		for y in range(3):
			if board[x][y] != '':
				img = pg.image.load('{}.jpg'.format(board[x][y]))
				screen.blit(img, [60 + y * 100, 160 + x * 100])
	pg.display.update()

"""
	isFree - return True if the place is free on the board.
	@board: list 10 of string.
	@place: integer in range(1, 9).
"""
def isFree(board, place):
	return place[0] in range(3) and place[1] in range(3) and board[place[0]][place[1]] == ''


"""
	takeMove - place a chess on the board.
	@board: list 10 of string.
	@place: integer in range(1, 9).
	@chess: string

	Return False if the place on the board is already have chest.
"""
def takeMove(board, place, chess):
	if isFree(board, place):
		board[place[0]][place[1]] = chess
		return True
	else:
		return False



"""
	Move - ask the user where he wants to play chess.
	@board: list 10 of string.
	@chess: string
"""
def Move(screen, board, chess):
	x, y = -1, -1
	while not takeMove(board, (x, y), chess):
		for event in pg.event.get():
			if event.type == pg.MOUSEBUTTONDOWN:
				mx, my = pg.mouse.get_pos()
				y = int((mx - 50) / 100)
				x = int((my - 150) / 100)
	return

"""
	updateState - update the game state of player wining.
	@board: list 10 of string.

	store the result in the board[0].
"""
def updateState(board):
	game_state = ' '
	def theSame(a, b, c):
		return a == b and b == c
	# check if the player has won the game.
	## raw
	if theSame(board[0][0], board[0][1], board[0][2]): game_state = board[0][0]
	elif theSame(board[1][0], board[1][1], board[1][2]): game_state = board[1][0]
	elif theSame(board[2][0], board[2][1], board[2][2]): game_state = board[2][0]
	## column
	elif theSame(board[0][0], board[1][0], board[2][0]): game_state = board[0][0]
	elif theSame(board[0][1], board[1][1], board[2][1]): game_state = board[0][1]
	elif theSame(board[0][2], board[1][2], board[2][2]): game_state = board[0][2]
	## diagonal
	elif theSame(board[0][0], board[1][1], board[2][2]): game_state = board[0][0]
	elif theSame(board[0][2], board[1][1], board[2][0]): game_state = board[0][2]
	return game_state

"""
	haveWinner - return True if any player has won the game.
	@board: list 10 of string.
"""
def haveWinner(game_state):
	return game_state == 'X' or game_state == 'O'


"""
OAO
"""
def GetPlayerChess(screen):
	player_chess = None
	while player_chess == None:
		for event in pg.event.get():
			if event.type == pg.MOUSEBUTTONDOWN:
				mx, my = pg.mouse.get_pos()
				if mx in range(87, 171) and my in range(340, 427):
					player_chess = 'O'
				elif mx in range(228, 427) and my in range(340, 427):
					player_chess = 'X'
	return player_chess


""" Main function start here. """

screen, board = init()
chessSet = ['O', 'X']
turns = 0

player_chess = GetPlayerChess(screen)
screen.blit(pg.image.load('tictactoe_2.jpg'), [0, 0])
pg.display.update()

chessSet.remove(player_chess)
computer_chess = chessSet[0]
game_state = ' '
while turns < 9:
	# player
	drawBoaard(screen, board)
	Move(screen, board, player_chess)
	drawBoaard(screen, board)
	game_state = updateState(board)
	if haveWinner(game_state): break
	turns = turns + 1
	if turns >= 9: break

	# computer
	tryboard, tryplace = None, None
	emptyplace = []
	for x in range(3):
		for y in range(3):
			if isFree(board, (x, y)):
				emptyplace.append((x, y))
	for eplace in emptyplace:
		tryboard = deepcopy(board)
		takeMove(tryboard, eplace, player_chess)
		if updateState(tryboard) == player_chess:
			tryplace = eplace
		tryboard = deepcopy(board)
		takeMove(tryboard, eplace, computer_chess)
		if updateState(tryboard) == computer_chess:
			tryplace = eplace
	if tryplace == None:
		tryplace = emptyplace[rand(0, len(emptyplace)-1)]

	takeMove(board, tryplace, computer_chess)
	drawBoaard(screen, board)
	game_state = updateState(board)
	if haveWinner(game_state): break
	turns = turns + 1
try:
	screen.blit(pg.image.load("{}win_img.jpg".format(game_state)), [100, 475])
	pg.display.update()
except:
	screen.blit(pg.image.load("tie_img.jpg"), [100, 475])
	pg.display.update()

sleep(1)
