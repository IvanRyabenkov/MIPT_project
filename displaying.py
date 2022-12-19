import pygame
from settings import *
from ray_casting import ray_casting
from map import mini_map

class Displaying:
    def __init__(self, screen, screen_minimap):
        self.screen = screen
        self.screen_minimap = screen_minimap
        self.font = pygame.font.SysFont('comicsansms', 18, bold=True)
        self.texture = pygame.image.load('6.png').convert()
        
    def background(self):
        pygame.draw.rect(self.screen, BLUE, (0, 0, WIDTH, HEIGHT / 2))
        pygame.draw.rect(self.screen, GREY, (0, HEIGHT / 2, WIDTH, HEIGHT / 2))

    def world(self, player_pos, player_angle):
        ray_casting(self.screen, player_pos, player_angle, self.texture)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, BLACK)
        self.screen.blit(render, FPS_POS)

    def mini_map(self, player):
        self.screen_minimap.fill(WHITE)
        pygame.draw.line(self.screen_minimap, GREEN, (player.x // MINIMAP_SCALE, player.y // MINIMAP_SCALE),
                         (player.x // MINIMAP_SCALE + 12 * math.cos(player.angle),
                          player.y // MINIMAP_SCALE + 12 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.screen_minimap, YELLOW, ( int(player.x // MINIMAP_SCALE), int(player.y // MINIMAP_SCALE)), 5)
        for x, y in mini_map:  #2д карта
            pygame.draw.rect(self.screen_minimap, GREY, (x, y, MINIMAP_PIX, MINIMAP_PIX))
        self.screen.blit(self.screen_minimap, (10, 10))
