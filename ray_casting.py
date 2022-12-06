import pygame
from map import game_map
from settings import *
def mapping(a, b):
    return (a // PIX) * PIX, (b // PIX) * PIX

def ray_casting(screen, player_pos, player_angle):
    x_0, y_0 = player_pos
    x_ul, y_ul = mapping(x_0, y_0)#x up left, y up left - координаты верхнего левого угла квадрата, в котором находится игрок
    current_angle = player_angle - FOV / 2
    for ray in range(NUM_RAYS):
        sin = math.sin(current_angle)
        cos = math.cos(current_angle)

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
        proj_height  = PROJECTION_k / depth #высота проекции
        color_depth = 255 / (1 + depth * depth * 0.0001) # добавление коэфффициента глубины для цвета стен, зависящего от расстояния
        color = (color_depth, color_depth /2, color_depth /2)  #преобразовани цвета с использованием коэффициента
        pygame.draw.rect(screen, color, (ray * SCALE, HEIGHT / 2 - proj_height // 2, SCALE, proj_height))
        current_angle += DELTA_ANGLE

