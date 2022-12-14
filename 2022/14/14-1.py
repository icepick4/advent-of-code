import sys


def read_file(filename):
    rocks = []
    max_x = 0
    max_y = 0
    with open(filename, 'r') as f:
        for line in f:
            actions = line.strip().split('->')
            for action in actions:
                current = action.split(',')
                if int(current[0]) > max_x:
                    max_x = int(current[0])
                if int(current[1]) > max_y:
                    max_y = int(current[1])
                rocks.append([int(current[0]), int(current[1])])
            rocks.append([])
    return rocks, max_x, max_y


def set_rocks(rocks, cave):
    for i in range(len(rocks) - 1):
        if rocks[i+1] == []:
            continue
        if rocks[i] == []:
            continue
        if rocks[i][0] == rocks[i+1][0]:
            if rocks[i][1] < rocks[i+1][1]:
                for j in range(rocks[i][1], rocks[i+1][1] + 1):
                    cave[j][rocks[i][0]] = '#'

            else:
                for j in range(rocks[i][1], rocks[i+1][1] - 1, -1):
                    cave[j][rocks[i][0]] = '#'
        else:
            if rocks[i][0] < rocks[i+1][0]:
                for j in range(rocks[i][0], rocks[i+1][0] + 1):
                    cave[rocks[i][1]][j] = '#'
            else:
                for j in range(rocks[i][0], rocks[i+1][0] - 1, -1):
                    cave[rocks[i][1]][j] = '#'
        if rocks[i] == rocks[i-1]:
            rocks[i] = rocks[i+1]
    return cave


def can_fall(x, y, cave):
    if x == len(cave) - 1:
        return False
    if cave[x+1][y] == '.':
        return True
    return False


def can_fall_diagonal_left(x, y, cave):
    if x == len(cave) - 1:
        return False
    if cave[x+1][y-1] == '.':
        return True
    return False


def can_fall_diagonal_right(x, y, cave):
    if x == len(cave) - 1:
        return False
    if cave[x+1][y+1] == '.':
        return True
    return False


def fall(x, y, cave, part):
    if x+1 == len(cave) or y+1 == len(cave[0]):
        return False if part == 1 else [x, y]
    if can_fall(x, y, cave):
        return [x+1, y]
    if can_fall_diagonal_left(x, y, cave):
        return [x+1, y-1]
    if can_fall_diagonal_right(x, y, cave):
        return [x+1, y+1]
    return [x, y]


def ending():
    COUNTER = 0
    for line in cave:
        COUNTER += line.count('O')
    print(COUNTER, 'units of sand come to rest')
    sys.exit()


if __name__ == '__main__':
    rocks, max_x, max_y = read_file('input.txt')
    part = 1
    if part == 2:
        cave = [['.' for _ in range(max_x + 150)] for _ in range(max_y + 2)]
    else:
        cave = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    cave = set_rocks(rocks, cave)
    start = [0, 500]
    cave[0][500] = '+'
    current_pos = start
    last_pos = []
    while True:
        while last_pos != current_pos:
            last_pos = current_pos
            current_pos = fall(current_pos[0], current_pos[1], cave, part)
            if part == 1:
                if current_pos is False:
                    ending()
            elif part == 2:
                if current_pos == [0, 500]:
                    cave[current_pos[0]][current_pos[1]] = 'O'
                    ending()
        cave[current_pos[0]][current_pos[1]] = 'O'
        current_pos = start
        last_pos = []
