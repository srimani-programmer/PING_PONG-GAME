# Ping-Pong game with turtle module.
# Done by @Sri_Programmer.
# Version - 3.7.0

__author__ = 'Sri Manikanta Palakollu'

import pygame
import sys 
import time
from pygame.locals import *
from random import randint

# pygame intialization
pygame.init()

WINDOW_WIDTH = 1024 # width of the game window
WINDOW_HEIGHT = 600 # height of the game window

clock = pygame.time.Clock() # to manipulate intervals 

player1_win = False # intial result for player1
player2_win = False # intial result for player2

# Paddle Code

PADDLE_SPEED = 10   # Moving Speed

# Intial movements for paddle1
UP1 = False 
DOWN1 = False
NO_MOVEMENT1 = True

# Initial movements for paddle2
UP2 = False
DOWN2 = False
NO_MOVEMENT2 = True

# Ball Code

UPLEFT = 0
DOWNLEFT = 1
UPRIGHT = 2
DOWNRIGHT = 3

# Music for the Game

pygame.mixer.music.load("/Users/srimanikanta/Desktop/Studies/PING_PONG-GAME/Sounds/endofline.ogg")
sound_effect = pygame.mixer.Sound("/Users/srimanikanta/Desktop/Studies/PING_PONG-GAME/Sounds/beep.wav")

BLACK = (0, 0, 0)   # window colour
WHITE = (255, 255, 255) # Paddle and ball colour

main_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32) # Game window
surface_rect = main_surface.get_rect()  # To handle the surface
pygame.display.set_caption('Ping-Pong Game')    # to set the window title


class Paddle(pygame.sprite.Sprite): # to create the paddles 

    def __init__(self, player_number):  # To create and Establish posistion of the paddle
        
        # Paddle Creation
        pygame.sprite.Sprite.__init__(self)
        self.player_number = player_number
        self.image = pygame.Surface([10, 100])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.speed = 8
        
        # Location of the paddle

        if self.player_number == 1:
            self.rect.centerx = main_surface.get_rect().left
            self.rect.centerx += 50
        elif self.player_number == 2:
            self.rect.centerx = main_surface.get_rect().right
            self.rect.centerx -= 50
        self.rect.centery = main_surface.get_rect().centery


    def move(self): # movement of the paddle with respect to the keys

        if self.player_number == 1:
            if (UP1 == True) and (self.rect.y > 5):
                self.rect.y -= self.speed
            elif (DOWN1 == True) and (self.rect.bottom < WINDOW_HEIGHT-5):
                self.rect.y += self.speed
            elif (NO_MOVEMENT1 == True):
                pass

        if self.player_number == 2:
            if (UP2 == True) and (self.rect.y > 5):
                self.rect.y -= self.speed
            elif (DOWN2 == True) and (self.rect.bottom < WINDOW_HEIGHT-5):
                self.rect.y += self.speed
            elif (NO_MOVEMENT2 == True):
                pass


class Ball(pygame.sprite.Sprite):   # to create the ball
    
    def __init__(self): # constructor to call itself
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([10, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = surface_rect.centerx
        self.rect.centery = surface_rect.centery
        self.direction = randint(0,3)
        self.speed = 4

    def move(self): # Ball movement method
        if self.direction == UPLEFT:
            self.rect.x -= self.speed
            self.rect.y -= self.speed
        elif self.direction == UPRIGHT:
            self.rect.x += self.speed
            self.rect.y -= self.speed
        elif self.direction == DOWNLEFT:
            self.rect.x -= self.speed
            self.rect.y += self.speed
        elif self.direction == DOWNRIGHT:
            self.rect.x += self.speed
            self.rect.y += self.speed

    def change_direction(self): # direction method
        if self.rect.y < 0 and self.direction == UPLEFT:
            self.direction = DOWNLEFT
        if self.rect.y < 0 and self.direction == UPRIGHT:
            self.direction = DOWNRIGHT
        if self.rect.y > surface_rect.bottom and self.direction == DOWNLEFT:
            self.direction = UPLEFT
        if self.rect.y > surface_rect.bottom and self.direction == DOWNRIGHT:
            self.direction = UPRIGHT

# Fonts for the game to display

basic_font = pygame.font.SysFont("Monaco", 60)   # Font on the main game window
game_over_font_big = pygame.font.SysFont("Helvetica", 72)
game_over_font_small = pygame.font.SysFont("Helvetica", 50)

# paddle objects for left and right side
paddle1 = Paddle(1)
paddle2 = Paddle(2)

# ball object
ball = Ball()

# 
all_sprites = pygame.sprite.RenderPlain(paddle1, paddle2, ball) 

player1_score = 0   # initial game score for player1
player2_score = 0   # initial game score for player2

def paddle_hit():    # operations on paddle

    if pygame.sprite.collide_rect(ball, paddle2):
        if (ball.direction == UPRIGHT):
            ball.direction = UPLEFT
        elif (ball.direction == DOWNRIGHT):
            ball.direction = DOWNLEFT
        ball.speed += 1
        sound_effect.play()
    elif pygame.sprite.collide_rect(ball, paddle1):
        if (ball.direction == UPLEFT):
            ball.direction = UPRIGHT
        elif (ball.direction == DOWNLEFT):
            ball.direction = DOWNRIGHT
        ball.speed +=1
        sound_effect.play()

    
counter = 0

while True:

    clock.tick(60)

    if (ball.rect.x > WINDOW_WIDTH):
        ball.rect.centerx = surface_rect.centerx
        ball.rect.centery = surface_rect.centery
        ball.direction = randint(0, 1)
        ball.speed = 4
    elif (ball.rect.x < 0):
        ball.rect.centerx = surface_rect.centerx
        ball.rect.centery = surface_rect.centery
        ball.direction = randint(2, 3)
        ball.speed = 4


    for event in pygame.event.get():    # to quit from the console window
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            
            if event.key == ord('u'):
                UP1 = True
                DOWN1 = False
                NO_MOVEMENT1 = False
            elif event.key == ord('d'):
                UP1 = False
                DOWN1 = True
                NO_MOVEMENT1 = False
                
            elif event.key == K_UP:
                UP2 = True
                DOWN2 = False
                NO_MOVEMENT2 = False
            elif event.key == K_DOWN:
                UP2 = False
                DOWN2 = True
                NO_MOVEMENT2 = False
                
            
        elif event.type == KEYUP:
            if event.key == ord('u') or event.key == ord('d'):
                NO_MOVEMENT1 = True
                DOWN1 = False
                UP1 = False
            elif event.key == K_DOWN or event.key == K_UP:
                NO_MOVEMENT2 = True
                DOWN2 = False
                UP2 = False


    score_board = basic_font.render('Player A: ' + str(player1_score) + "           " + 'Player B: '+ str(player2_score), True, WHITE, BLACK) 
    score_board_rect = score_board.get_rect()
    score_board_rect.centerx = surface_rect.centerx 
    score_board_rect.y = 10

    main_surface.fill(BLACK)

    main_surface.blit(score_board, score_board_rect)

    netx = surface_rect.centerx

    net_rect0 = pygame.Rect(netx, 0, 5, 5)
    net_rect1 = pygame.Rect(netx, 60, 5, 5)
    net_rect2 = pygame.Rect(netx, 120, 5, 5)
    net_rect3 = pygame.Rect(netx, 180, 5, 5)
    net_rect4 = pygame.Rect(netx, 240, 5, 5)
    net_rect5 = pygame.Rect(netx, 300, 5, 5)
    net_rect6 = pygame.Rect(netx, 360, 5, 5)
    net_rect7 = pygame.Rect(netx, 420, 5, 5)
    net_rect8 = pygame.Rect(netx, 480, 5, 5)
    net_rect9 = pygame.Rect(netx, 540, 5, 5)
    net_rect10 = pygame.Rect(netx, 595, 5, 5)
    
    pygame.draw.rect(main_surface, WHITE, (net_rect0.left, net_rect0.top, net_rect0.width, net_rect0.height))
    pygame.draw.rect(main_surface, WHITE, (net_rect1.left, net_rect1.top, net_rect1.width, net_rect1.height))
    pygame.draw.rect(main_surface, WHITE, (net_rect2.left, net_rect2.top, net_rect2.width, net_rect2.height))
    pygame.draw.rect(main_surface, WHITE, (net_rect3.left, net_rect3.top, net_rect3.width, net_rect3.height))
    pygame.draw.rect(main_surface, WHITE, (net_rect4.left, net_rect4.top, net_rect4.width, net_rect4.height))
    pygame.draw.rect(main_surface, WHITE, (net_rect5.left, net_rect5.top, net_rect5.width, net_rect5.height))
    pygame.draw.rect(main_surface, WHITE, (net_rect6.left, net_rect6.top, net_rect6.width, net_rect6.height))
    pygame.draw.rect(main_surface, WHITE, (net_rect7.left, net_rect7.top, net_rect7.width, net_rect7.height))
    pygame.draw.rect(main_surface, WHITE, (net_rect8.left, net_rect8.top, net_rect8.width, net_rect8.height))
    pygame.draw.rect(main_surface, WHITE, (net_rect9.left, net_rect9.top, net_rect9.width, net_rect9.height))
    pygame.draw.rect(main_surface, WHITE, (net_rect10.left, net_rect10.top, net_rect10.width, net_rect10.height))


    all_sprites.draw(main_surface)

    paddle1.move()
    paddle2.move()
    ball.move()
    ball.change_direction()

    paddle_hit()

    if ball.rect.x > WINDOW_WIDTH:
        player1_score += 1
    elif ball.rect.x < 0:
        player2_score += 1


    pygame.display.update() # display update

    if counter == 0:
        time.sleep(1.5)
        pygame.mixer.music.play(-1, 0.5)

    if player1_score == 5:
        player1_win = True
        break
    elif player2_score == 5:
        player2_win = True
        break

    counter += 1

while True:

    for event in pygame.event.get():    # to quit from the pygame
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    main_surface.fill(BLACK)

    if player1_win == True: # winning code for player1
        game_over = game_over_font_big.render("GAME OVER", True, WHITE, BLACK)
        game_over1 = game_over_font_small.render("Winner is Player A", True, WHITE, BLACK)
    elif player2_win == True:   # winning code for player2
        game_over = game_over_font_big.render("GAME OVER", True, WHITE, BLACK)
        game_over1 = game_over_font_small.render("Winner is Player B", True, WHITE, BLACK)

    game_over_rect = game_over.get_rect()
    game_over_rect.centerx = surface_rect.centerx
    game_over_rect.centery = surface_rect.centery - 50
    game_over1_rect = game_over1.get_rect()
    game_over1_rect.centerx = game_over_rect.centerx
    game_over1_rect.centery = game_over_rect.centery + 75

    main_surface.blit(game_over, game_over_rect)
    main_surface.blit(game_over1, game_over1_rect)

    pygame.display.update()

