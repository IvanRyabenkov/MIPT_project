from settings import *

text_map = [        # карта, где '.'-пустое пространство, '1' - стена
    '1111111111111111',
    '1....1.....1...1',
    '1..............1',
    '1...11.........1',
    '1.......11....11',
    '1....1.....1...1',
    '1.....111......1',
    '1..........11..1',
    '1..11..........1',
    '1..........11..1',
    '1.....1....1.1.1',
    '1111111111111111'
]

game_map = set()
mini_map = set()
for i, row in enumerate(text_map):
    for j, obst in enumerate(row):
        if obst == '1':
            game_map.add((j * PIX, i * PIX))
            mini_map.add((j * MINIMAP_PIX, i * MINIMAP_PIX))
