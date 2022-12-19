from settings import *
import random
import pygame
def invert(a):
    k = ''
    for i in range(len(a)):
        if a[i] == "1":
            k += "1"
        else:
            k += '0'
    return k

def start_point_generate(n, m):
    return (0,0)


def finish_point_generate(start, n, m):
    """Выбор точки конца лабиринта"""
    return n - 1 - start[0], m - 1 - start[1]
def transition_choice(x, y, rm):
    """Функция выбора дальнейшего пути в генерации лабиринта"""
    choice_list = []
    if x > 0:
        if not rm[x - 1][y]:
            choice_list.append((x - 1, y))
    if x < len(rm) - 1:
        if not rm[x + 1][y]:
            choice_list.append((x + 1, y))
    if y > 0:
        if not rm[x][y - 1]:
            choice_list.append((x, y - 1))
    if y < len(rm[0]) - 1:
        if not rm[x][y + 1]:
            choice_list.append((x, y + 1))
    if choice_list:
        nx, ny = random.choice(choice_list)
        if x == nx:
            if ny > y:
                tx, ty = x * 2, ny * 2 - 1
            else:
                tx, ty = x * 2, ny * 2 + 1
        else:
            if nx > x:
                tx, ty = nx * 2 - 1, y * 2
            else:
                tx, ty = nx * 2 + 1, y * 2
        return nx, ny, tx, ty
    else:
        return -1, -1, -1, -1

def create_labyrinth(n = 5, m = 5):
    """Генерация лабиринта"""
    reach_matrix = []
    for i in range(n):  # создаём матрицу достижимости ячеек
        reach_matrix.append([])
        for j in range(m):
            reach_matrix[i].append(False)
    transition_matrix = []
    for i in range(n * 2 - 1):  # заполнение матрицы переходов
        transition_matrix.append([])
        for j in range(m * 2 - 1):
            if i % 2 == 0 and j % 2 == 0:
                transition_matrix[i].append(True)
            else:
                transition_matrix[i].append(False)
    start = start_point_generate(n, m)
    finish = finish_point_generate(start, n, m)
    list_transition = [start]
    x, y = start
    reach_matrix[x][y] = True
    x, y, tx, ty = transition_choice(x, y, reach_matrix)
    for i in range(1, m * n):
        while not (x >= 0 and y >= 0):
            x, y = list_transition[-1]
            list_transition.pop()
            x, y, tx, ty = transition_choice(x, y, reach_matrix)
        reach_matrix[x][y] = True
        list_transition.append((x, y))
        transition_matrix[tx][ty] = True
        x, y, tx, ty = transition_choice(x, y, reach_matrix)
    return transition_matrix, start, finish  # возвращаем матрицу проходов,начальную и конечную точку


mapp = list(create_labyrinth(nn, mm))
startpos = mapp[-2]
endpos = mapp[-1]
mapp.pop()
mapp.pop()
MAP = []
MAPP = []
for i in range(nn):
    MAP.append(mapp[0][i][:])
for i in range(len(MAP)):
    MAP[i] = str(MAP[i]).replace("True","0")
    MAP[i] = str(MAP[i]).replace("False","1")
for i in range(len(MAP)):
    a = "".join(MAP[i])
    s = ""
    for j in range(len(a)):
        if a[j] == "0" or a[j] == "1":
            s += a[j]
    MAPP.append(s)

mapp = [ "0" + "1"*(2*nn), "10"+invert(MAPP[2]) + '01']
for i in range(len(MAPP)):

    mapp.append("10"+MAPP[i] + "01")
mapp.append("1"+"11" + "0"*(2*nn)+"1")
mapp.append("1"*(2*nn + 4))

text_map = mapp
print(mapp)

game_map = set()
mini_map = set()
collision_walls = []

for i, row in enumerate(text_map):
    for j, obst in enumerate(row) :
        if obst == '1':
            game_map.add((j * PIX, i * PIX))
            mini_map.add((j * MINIMAP_PIX, i * MINIMAP_PIX))
            collision_walls.append(pygame.Rect(j * PIX, i * PIX, PIX, PIX))
print(endpos)