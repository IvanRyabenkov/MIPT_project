import pygame
import math
import numpy as np
from settings import *
from player import Player
from map import game_map
from map import mini_map
from ray_casting import ray_casting
from displaying import Displaying

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_minimap = pygame.Surface((WIDTH * 1.5 // MINIMAP_SCALE, HEIGHT * 1.5 // MINIMAP_SCALE))
clock = pygame.time.Clock()
player = Player()
displaying = Displaying(screen, screen_minimap)



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()
    screen.fill(BLACK)
    displaying.background()
    displaying.world(player.pos(), player.angle)
    displaying.mini_map(player)





    #displaying.fps(clock)


    pygame.display.flip()
    clock.tick(FPS)
