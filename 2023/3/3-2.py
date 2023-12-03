def read_file(filename):
    engine = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            engine.append([])
            for char in line:
                if char == '\n':
                    continue
                engine[-1].append(char)
    gears = []
    for i, line in enumerate(engine):
        current_number = ''
        current_number_is_adjacent = False
        for j, char in enumerate(line):
            if char.isdigit():
                current_number += char
                if not current_number_is_adjacent:
                    current_number_is_adjacent, gear_position = is_adjacent(i, j, engine)
            else:
                if current_number_is_adjacent:
                    gears = adding_gear(gear_position, int(current_number), gears)
                current_number = ''
                current_number_is_adjacent = False
        if current_number_is_adjacent and current_number != '':
            gears = adding_gear(gear_position, int(current_number), gears)
    print(calculate_result(gears))

def adding_gear(gear_position, value, gears):
    added = False
    for i in gears:
        if i[0] == gear_position:
            i[1].append(value)
            added = True
    if not added:
        gears.append([gear_position, [value]])
    return gears

def calculate_result(gears):
    sum = 0
    for i in gears:
        if len(i[1]) == 2:
            sum += i[1][0] * i[1][1]
    return sum

def is_adjacent(x, y, tab):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(tab) and 0 <= new_y < len(tab[0]):
            if tab[new_x][new_y] == '*':
                return True, (new_x, new_y)
    return False, None
    

if __name__ == '__main__':
    read_file('input.txt')