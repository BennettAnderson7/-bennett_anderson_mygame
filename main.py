# file created by: Bennett Anderson 11/7/23
# content from kids can code: http://kidscancode.org/blog/

# GameDesign: Platformer, mario style

'''
Goals: 
    - Create a class of mario style question blocks that are breakable upon impact from underneath
    - Implement textures to platforms, blocks, and the player
    - Have overall score affected by the breaking of blocks

'''

# Rules: No fleshed out rules for the game, purely trying to implement stated goals
# Feedback: Very difficult and finicky, specifically making the block break



# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from settings import *
from sprites import *

vec = pg.math.Vector2

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')
snd_folder = os.path.join(game_folder, 'sounds')

# define game class
class Game:
    def __init__(self):
        # init pygame and create a window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Game...")
        self.clock = pg.time.Clock()
        self.running = True
    
    def new(self):
        # create a group for all sprites
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.all_platforms = pg.sprite.Group()
        self.all_blocks = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()
        # instantiate classes
        self.player = Player(self)
        # add instances to groups
        self.all_sprites.add(self.player)

        for p in PLATFORM_LIST:
            # instantiation of the Platform class
            plat = Platform(*p)
            self.all_sprites.add(plat)
            self.all_platforms.add(plat)

        for b in BLOCK_LIST: 
            # instantiation of the block class
            blok = Block(*b)
            self.all_sprites.add(blok)
            self.all_blocks.add(blok)

        # took out mobs
        '''for m in range(0,10):
            m = Mob(randint(0, WIDTH), randint(0, HEIGHT/2), 20, 20, "normal")
            self.all_sprites.add(m)
            self.all_mobs.add(m)'''
        

        self.run()
    
    # create clock and update
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

        # this is what prevents the player from falling through the platform when falling down...
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
                self.player.vel.x = hits[0].speed*1.5

        # this is what prevents the player from falling through the block when falling down...
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.all_blocks, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
                self.player.vel.x = hits[0].speed*1.5      

         # this is what enables the player to break the block from underneath...
        if self.player.vel.y < 0:
            hits = pg.sprite.spritecollide(self.player, self.all_blocks, True)
            if hits:
                self.player.pos.y = hits[0].rect.bottom
                self.player.vel.y = 5
                self.player.vel.x = hits[0].speed*1.5    
                self.score += 1
        ''' # this prevents the player from jumping up through a platform
        if self.player.vel.y < 0:
            hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
            if hits:
                print("ouch")
                self.score -= 1
                if self.player.rect.bottom >= hits[0].rect.top - 1: 
                    self.player.acc.y = -5
                    self.player.vel.y = 0
                if self.player.rect.top >= hits[0].rect.bottom - 1:
                    self.player.acc.y = -5
                    self.player.vel.y = 0'''
        '''
        if self.player.pos.x > WIDTH/2:
            for p in self.all_platforms:
                p.rect.x += 1
'''

    def events(self):
        for event in pg.event.get():
        # check for closed window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                
    def draw(self):
        ############ Draw ################
        # draw the background screen
        self.screen.fill(BLACK)
        # draw all sprites
        self.all_sprites.draw(self.screen)
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH/2, HEIGHT/10)
        # buffer - after drawing everything, flip display
        pg.display.flip()
    
    # insert text
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass

g = Game()
while g.running:
    g.new()


pg.quit()
