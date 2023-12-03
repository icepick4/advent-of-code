def read_file(filename):
    engine = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            engine.append([])
            for char in line:
                if char == '\n':
                    continue
                engine[-1].append(char)
    sum = 0
    for i, line in enumerate(engine):
        current_number = ''
        current_number_is_adjacent = False
        for j, char in enumerate(line):
            if char.isdigit():
                current_number += char
                if is_adjacent(i, j, engine):
                    current_number_is_adjacent = True
            else:
                if current_number_is_adjacent:
                    sum += int(current_number)
                current_number = ''
                current_number_is_adjacent = False
        if current_number_is_adjacent and current_number != '':
            sum += int(current_number)
    print(sum)
                

def is_adjacent(x, y, tab):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(tab) and 0 <= new_y < len(tab[0]):
            if not tab[new_x][new_y].isdigit() and tab[new_x][new_y] != '.' :
                return True
    return False
    

if __name__ == '__main__':
    read_file('input.txt')