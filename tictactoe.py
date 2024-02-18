#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pygame
import math


# In[11]:


CIRCLE=pygame.image.load('circle.png')
CROSS=pygame.image.load('x.png')
RED=(255,0,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
ROWS=3
COLUMNS=3
SQUARE=200
WIDTH=600
HEIGHT=600
SIZE=(WIDTH,HEIGHT)
CIRCLE=pygame.image.load('circle.png')
X=pygame.image.load('x.png')
game_over=False
turn=0
board=np.zeros((ROWS,COLUMNS))


# In[12]:


def is_valid_mark(row,col):
    return board[row][col]==0


# In[13]:


def mark(row,col,player):
    board[row][col]=player


# In[14]:


def is_board_full():
    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c]==0:
                return False
    return True


# In[15]:


def is_winning_move(player):
    if player== 1:
        color=BLUE
    else:
        color=RED
    for r in range(ROWS):
        if board[r][0]==player and board[r][1]==player and board[r][2]==player:
            pygame.draw.line(window,color,(10,(r*200)+100),(WIDTH-10,(r*200)+100),10)
            return True
    for c in range(COLUMNS):
        if board[0][c]==player and board[1][c]==player and board[2][c]==player:
            pygame.draw.line(window,color,((c*200)+100,10),((c*200)+100,HEIGHT-10),10)
            return True
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        pygame.draw.line(window,color,(10,10),(590,590),10)
        return True
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
        pygame.draw.line(window,color,(590,10),(10,590),10)
        return True


# In[16]:


def draw_board():
    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c]==1:
                window.blit(CIRCLE,((c*200)+50,(r*200)+50))
            elif board[r][c]==2:
                window.blit(X,((c*200)+50,(r*200)+50))
    pygame.display.update()


# In[17]:


def draw_lines():
    pygame.draw.line(window,BLACK,(200,0),(200,600),10)
    pygame.draw.line(window,BLACK,(400,0),(400,600),10)
    pygame.draw.line(window,BLACK,(0,200),(600,200),10)
    pygame.draw.line(window,BLACK,(0,400),(600,400),10)


# In[18]:


pygame.init()
window=pygame.display.set_mode(SIZE)
pygame.display.set_caption("Tic-Tac-Toe")
window.fill(WHITE)
draw_lines()
pygame.display.update()
pygame.time.wait(2000)
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if turn%2==0:
                #player1
                row=math.floor(event.pos[1]/200)
                col=math.floor(event.pos[0]/200)
                if is_valid_mark(row,col):
                    mark(row,col,1)
                    if is_winning_move(1):
                        game_over=True
                else:
                    turn-=1
            else:
                #player2
                row=math.floor(event.pos[1]/200)
                col=math.floor(event.pos[0]/200)
                if is_valid_mark(row,col):
                    mark(row,col,2)
                    if is_winning_move(2):
                        game_over=True
                else:
                    turn-=1
            turn+=1
            print(board)
            draw_board()
    if is_board_full():
        game_over=True
    if game_over==True:
        print("Game Over")
        pygame.time.wait(2000)
        board.fill(0)
        window.fill(WHITE)
        draw_lines()
        draw_board()
        game_over=False
        pygame.display.update()


# In[ ]:




