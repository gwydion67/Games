import numpy as np
import pygame
import sys
import math

ROW_COUNT = 6
COLUMN_COUNT = 7

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

SQUARE_SIZE = 100
RADIUS = int(SQUARE_SIZE/2 - 5)


width = COLUMN_COUNT * SQUARE_SIZE
height = (ROW_COUNT + 1) * SQUARE_SIZE
size = (width, height)
pygame.init()
screen = pygame.display.set_mode(size)

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board,col):
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r
        
def print_board(board):
    print(np.flip(board, 0))
    
def winning_move(board, piece):
    for c in range(COLUMN_COUNT - 3 ):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece :
                return True
    
    for c in range(COLUMN_COUNT ):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece :
                return True
   
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece :
                return True
    
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT - 3):
            if board[r][c] == piece and board[r-1][c-1] == piece and board[r-2][c-2] == piece and board[r-3][c-3] == piece :
                return True

def draw_board(board):
	pygame.display.update()
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			pygame.draw.rect(screen, BLUE, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
			pygame.draw.circle(screen, BLACK, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), int(r*SQUARE_SIZE+SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)		
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			if board[r][c] == 1:
				pygame.draw.circle(screen, RED, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), height - int(r*SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
			elif board[r][c] == 2:
				pygame.draw.circle(screen, YELLOW, (int(c*SQUARE_SIZE+SQUARE_SIZE/2), height - int(r*SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
	pygame.display.update()





def connect4():
    board = create_board()
    print_board(board)    
    draw_board(board)
    game_over = False
    myfont = pygame.font.SysFont("monospace", 75)
    turn = 0 

    while not game_over:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.MOUSEMOTION:
                posx = event.pos[0]
                pygame.draw.rect(screen, BLACK,(0,0,width, SQUARE_SIZE)) 
                if(turn == 0):
                    pygame.draw.circle(screen, RED, (posx,int(SQUARE_SIZE/2)), RADIUS)
                else:
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARE_SIZE/2)), RADIUS)
                    
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK,(0,0,width, SQUARE_SIZE)) 
                posx = event.pos[0]
                
                #Ask player 1 input
                if turn == 0:
                    col = int(math.floor(posx/SQUARE_SIZE))
                    
                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)
                        
                        if winning_move(board, 1):
                            label = myfont.render("Player 1 wins!!", 1,(2), RED)
                            screen.blit(label, (40,10))
                            game_over = True
                #Ask player 2 input
                if turn == 1:
                    col = int(math.floor(posx/SQUARE_SIZE))
                    
                    if is_valid_location(board , col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)
                    
                        if winning_move(board, 2):
                            label = myfont.render("Player 2 wins!!", 1,(2), YELLOW)
                            screen.blit(label, (40,10))
                            game_over = True
            
                turn +=1
                turn %= 2
            print_board(board)   
            draw_board(board) 
            if(game_over):
                pygame.time.wait(2000)



if __name__ =="__main__":
    connect4()