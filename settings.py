import math
import numpy as np

WIDTH = 1000
HEIGHT = 600
FPS = 120
PIX = 25
FPS_POS = (WIDTH - 50, 10)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, GREY]

nn =(WIDTH // PIX) // 2 - 4
mm = (HEIGHT // PIX) // 2 - 4

player_pos = ((WIDTH // nn), (HEIGHT // mm))
player_angle = math.pi / 2
player_speed = 2

FOV = math.pi / 3 #field of views
NUM_RAYS = 500
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
SCALE = WIDTH // NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(FOV/2))
PROJECTION_k = 3 * DIST * PIX

MINIMAP_SCALE = 5
MINIMAP_PIX =PIX // MINIMAP_SCALE

TIME_POS = (WIDTH - 150, 20)
TIMER_POS = (WIDTH - 100, 20)