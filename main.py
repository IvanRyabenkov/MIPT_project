import fontTools.fontBuilder
import pygame
import math
import numpy as np
import sys
from settings import *
from player import Player
from map import game_map
from map import mini_map
from ray_casting import ray_casting
from ray_casting import mapping
from displaying import Displaying
from map import endpos

pygame.init()
#music_settings
pygame.mixer.music.load("sounds/music2.mp3")
pygame.mixer.music.set_volume(0.1)
#screen setthings and minimap
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_minimap = pygame.Surface((WIDTH * 1.05 // MINIMAP_SCALE, HEIGHT * 1.7 // MINIMAP_SCALE))
clock = pygame.time.Clock()
player = Player()
displaying = Displaying(screen, screen_minimap)

#Menu class
class Menu:
    def __init__(self, punckts = [120, 140, "Punkt", (250, 250, 250), (250,30,250)]):
        self.punkts = punckts
    def render(self, poverhnost, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))
    def menu(self):
        done = True
        font_menu = pygame.font.SysFont('arial', 144)
        punkt = 0
        while done:
            screen.fill((0,100, 200))
            np = pygame.mouse.get_pos()
            for i in self.punkts:
                if np[0]>i[0] and np[0]<i[0] + 55 and np[1]>i[1] and np[1] <i[1] + 50:
                    punkt = i[5]
                self.render(screen, font_menu, punkt)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if  e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts)-1:
                            punkt += 1
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        sys.exit()

            screen.blit(screen, ((0, 0)))
            pygame.display.flip()


punkts = [(500, 200, "Game", (250, 250, 30), (250, 30, 250), 0),
          (500, 400, "Quit",(250, 250, 30), (250,30,250),1) ]
game = Menu(punkts)
game.menu()




pygame.mixer.music.play(loops = -1, start = 0.0, fade_ms = 0)

running = True
#main cycle
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    screen.fill(BLACK)
    displaying.background()
    displaying.world(player.pos(), player.angle)
    displaying.timer()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_g]:
        displaying.mini_map(player)
        SCORE -= DELTA_SCORE
    #print(SCORE)
    x, y = player.pos()
    x_end, y_end = endpos[0], endpos[1]
    if (mapping(x, y)) == mapping(1150, 1250):
        game.menu()


    #displaying.fps(clock)
    displaying.timer()

    pygame.display.flip()
    clock.tick(FPS)
quit()