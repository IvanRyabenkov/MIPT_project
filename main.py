import pygame
import math
import numpy as np
from settings import *
from player import Player
from map import game_map
from map import mini_map
from ray_casting import ray_casting
from displaying import Displaying
global lol
lol = 0
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_minimap = pygame.Surface((WIDTH * 1.05 // MINIMAP_SCALE, HEIGHT * 1.7 // MINIMAP_SCALE))
clock = pygame.time.Clock()
player = Player()
displaying = Displaying(screen, screen_minimap)

class Menu:
    def __init__(self):
        self._option_surfaces = []
        self._callbacks = []
        self._current_option_index = []

    def append_option(self, option):







while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()
    screen.fill(BLACK)
    displaying.background()
    displaying.world(player.pos(), player.angle)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_g]:
        displaying.mini_map(player)
        lol += 0.01
    print(lol)

    #displaying.fps(clock)


    pygame.display.flip()
    clock.tick(FPS)
