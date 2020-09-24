import pygame as pg
from random import randint as rand
import sys

pg.init()

def firstpage():

	screen = pg.display.set_mode((400, 600))
	pg.display.set_caption('tictactoe_v1.1')
	screen.fill((255, 255, 255))
	bg = pg.image.load('tictactoe_1.jpg')
	screen.blit(bg, [0, 0])
	while True:
		for event in pg.event.get():
			if event.type == pg.MOUSEBUTTONDOWN:
				mouse = pg.mouse.get_pos()
				if mouse[0] in range(87, 171) and mouse[1] in range(340, 427):
					pg.quit()
					return 'O'
				if mouse[0] in range(228, 427) and mouse[1] in range(340, 427):
					pg.quit()
					return 'X'

			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			pg.display.update()

def drawBoard(board):

    for block_y in range(3):
    	for block_x in range(3):
    		if theBoard[block_x][block_y] == 'X':
    			X = pg.image.load('X.jpg')
    			screen.blit(X, [60 + block_y * 100, 160 + block_x * 100])
    		if theBoard[block_x][block_y] == 'O':
    			O = pg.image.load('O.jpg')
    			screen.blit(O, [60 + block_y * 100, 160 + block_x * 100])

def getMove(board, chest, move_x, move_y):
    theBoard[move_y][move_x] = chest

def isSpaceFree(board, move_x, move_y):
    # Return true if the passed move is free on the passed board.
    return move_x in range(3) and move_y in range(3) and board[move_y][move_x] == ' '

def isWinner(board, turn):
    return ((board[0][0] == turn and board[0][1] == turn and board[0][2] == turn) or
    (board[1][0] == turn and board[1][1] == turn and board[1][2] == turn) or
    (board[2][0] == turn and board[2][1] == turn and board[2][2] == turn) or
    (board[0][0] == turn and board[1][0] == turn and board[2][0] == turn) or
    (board[0][1] == turn and board[1][1] == turn and board[2][1] == turn) or
    (board[0][2] == turn and board[1][2] == turn and board[2][2] == turn) or
    (board[0][0] == turn and board[1][1] == turn and board[2][2] == turn) or
    (board[0][2] == turn and board[1][1] == turn and board[2][0] == turn))

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(3):
    	for j in range(3):
    		if isSpaceFree(board, i, j):
    			return False
    return True

user_turn = firstpage()
theBoard = [[' ', ' ', ' '],
			[' ', ' ', ' '],
			[' ', ' ', ' ']]

screen = pg.display.set_mode((400, 600))
pg.display.set_caption('tictactoe_v1.1')
screen.fill((255, 255, 255))
clock = pg.time.Clock()
bg = pg.image.load('tictactoe_2.jpg')
screen.blit(bg, [0, 0])
turn = "User"
chessSet = ['O', 'X']
chessSet.remove(user_turn)
computer_turn = chessSet[0]


while True:
	for event in pg.event.get():
		if turn == 'User':
			drawBoard(theBoard)
			if event.type == pg.MOUSEBUTTONDOWN:
				mouse = pg.mouse.get_pos()
				if mouse[0] in range(50, 350) and mouse[1] in range(150, 450):
					move_x = int((mouse[0] - 50) / 100)
					move_y = int((mouse[1] - 150) / 100)
					if isSpaceFree(theBoard, move_x, move_y):
						getMove(theBoard, user_turn, move_x, move_y)
						if isWinner(theBoard, user_turn):
							winner = user_turn
							turn = 'over'
						elif isBoardFull(theBoard):
							turn = 'tie'
						else:
							turn = 'Computer'

		elif turn == 'Computer':
			drawBoard(theBoard)
			tryplace = rand(1, 9)
			while not isSpaceFree(theBoard, tryplace % 3, tryplace // 3):
				tryplace = rand(1, 9)
			getMove(theBoard, computer_turn, tryplace % 3, tryplace // 3)
			if isWinner(theBoard, computer_turn):
				winner = computer_turn
				turn = 'over'
			elif isBoardFull(theBoard):
				turn = 'tie'
			else:
				turn = 'User'

		elif turn == 'over':
			drawBoard(theBoard)
			if winner == user_turn:
				Xwin_img = pg.image.load('Xwin_img.jpg')
				screen.blit(Xwin_img, [100, 475])
			else:
				Owin_img = pg.image.load('Owin_img.jpg')
				screen.blit(Owin_img, [100, 475])

		elif turn == 'tie':
			drawBoard(theBoard)
			tie_img = pg.image.load('tie_img.jpg')
			screen.blit(tie_img, [100, 475])

	if event.type == pg.QUIT:
		pg.quit()
		sys.exit()
	pg.display.update()
