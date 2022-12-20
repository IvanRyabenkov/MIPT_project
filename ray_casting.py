import pygame
from map import game_map
from settings import *

def mapping(a, b):
    return (a // PIX) * PIX, (b // PIX) * PIX

def ray_casting(screen, player_pos, player_angle, texture):

    x_0, y_0 = player_pos
    x_ul, y_ul = mapping(x_0, y_0)#x up left, y up left - координаты верхнего левого угла квадрата, в котором находится игрок
    current_angle = player_angle - FOV / 2

    for ray in range(NUM_RAYS):
        sin = math.sin(current_angle)
        cos = math.cos(current_angle)
        sin = sin if sin else 0.000001
        cos = cos if cos else 0.000001

        x, dx = (x_ul + PIX , 1) if cos >= 0 else (x_ul,-1)
        for i in range(0,WIDTH, PIX):
            depth_v = (x - x_0)/cos
            yv = y_0 + depth_v*sin
            if mapping(x + dx, yv) in game_map:
                break
            x += dx * PIX

        y, dy = (y_ul + PIX, 1) if sin >= 0 else(y_ul,-1)
        for i in range(0, HEIGHT, PIX):
            depth_h = (y - y_0)/sin
            xh = x_0 + depth_h*cos
            if mapping(xh, y + dy) in game_map:
                break
            y += dy * PIX

        depth, offset = (depth_v, yv) if depth_v < depth_h else (depth_h, xh)
        offset = int(offset) % PIX
        depth *= math.cos(player_angle - current_angle)
        depth = max(depth, 0.00001)
        proj_height = min(int(PROJECTION_k / depth), 2 * HEIGHT)

        wall_column = texture.subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
        wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
        screen.blit(wall_column, (ray * SCALE, HEIGHT//2 - proj_height // 2))

        current_angle += DELTA_ANGLE
        
        offset = int(offset) % PIX
        wall_column = texture.subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_H) # выдялем подповерхность в виде квадрата, где начальные координаты равны смещению и нач условиями
        wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
        screen.blit(wall_column, (ray * SCALE, (HEIGHT // 2) - proj_height // 2))
