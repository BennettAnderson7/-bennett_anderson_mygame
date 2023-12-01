# This file was created by: Bennett Anderson
# Content from Chris Bradfield; Kids Can Code
# KidsCanCode - Game Development with Pygame video series
# Video link: https://youtu.be/OmlQ0XCvIn0 

# game settings 
WIDTH = 480
HEIGHT = 360
FPS = 30

# player settings
PLAYER_JUMP = 30
PLAYER_GRAV = 1.5
global PLAYER_FRIC
PLAYER_FRIC = 0.2

# define colors (added some experimentally)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (112, 96, 65)
GOLD = (196, 135, 16)

# placement location of platforms
PLATFORM_LIST = [(40, HEIGHT - 40, WIDTH, 40, "normal"),(200, HEIGHT - 200, WIDTH, 40, "normal")]

# placement location of blocks
BLOCK_LIST = [(100, HEIGHT - 200, WIDTH, 40),(300, HEIGHT - 330, WIDTH, 40)]

                 

'''
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20,"normal"),
                 (125, HEIGHT - 350, 100, 20, "moving"),
                 (222, 200, 100, 20, "normal"),
                 (175, 100, 50, 20, "normal")]
                 '''