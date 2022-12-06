import pygame
import math
from settings import *

class Player():
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += player_speed * math.cos(self.angle)
            self.y += player_speed * math.sin(self.angle)
        if keys[pygame.K_s]:
            self.x += -player_speed * math.cos(self.angle)
            self.y += -player_speed * math.sin(self.angle)
        if keys[pygame.K_a]:
            self.x += player_speed * math.sin(self.angle)
            self.y += -player_speed * math.cos(self.angle)
        if keys[pygame.K_d]:
            self.x += -player_speed * math.sin(self.angle)
            self.y += player_speed * math.cos(self.angle)
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02


    def pos(self):
        return (self.x, self.y)