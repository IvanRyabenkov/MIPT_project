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

        if cos >= 0:
            x = x_ul + PIX
            dx = 1
        else:
            x = x_ul
            dx = -1
        for i in range(0, WIDTH, PIX):
            depth_v = (x - x_0) / cos
            y = y_0 + depth_v * sin
            if mapping(x+dx, y) in game_map:
                break
            x += dx * PIX

        if sin >= 0:
            y = y_ul + PIX
            dy = 1
        else:
            y = y_ul
            dy = -1
        for i in range(0, HEIGHT, PIX):
            depth_h = (y - y_0) / sin
            x = x_0 + depth_h * cos
            if mapping(x, y+dy) in game_map:
                break
            y += dy * PIX

        if depth_v < depth_h:
            depth = depth_v
        else:
            depth = depth_h

        depth *= math.cos(player_angle - current_angle)  # устранение неровностей стен
        depth = max(depth, 0.001)
        proj_height = min((PROJECTION_k / depth), 2 * HEIGHT) #высота проекции
        color_depth = 255 / (1 + depth ** 2 * 0.0001) # добавление коэфффициента глубины для цвета стен, зависящего от расстояния
        color = (color_depth, color_depth , color_depth /2 )  #преобразовани цвета с использованием коэффициента
        pygame.draw.rect(screen, color, (ray * SCALE, HEIGHT / 2 - proj_height // 2, SCALE, proj_height))
        current_angle += DELTA_ANGLE
        
        offset = int(offset) % PIX
        wall_column = texture.subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_H) # выдялем подповерхность в виде квадрата, где начальные координаты равны смещению и нач условиями
        wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
        screen.blit(wall_column, (ray * SCALE, (HEIGHT // 2) - proj_height // 2))
