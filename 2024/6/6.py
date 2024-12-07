def read_file(filename):
    map_area = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            map_area.append(list(line.strip()))

    return map_area

def next_direction(current_direction):
    if current_direction == (-1, 0):
        return (0, 1)
    if current_direction == (0, 1):
        return (1, 0)
    if current_direction == (1, 0):
        return (0, -1)
    if current_direction == (0, -1):
        return (-1, 0)
    

if __name__ == '__main__':
    map_area = read_file('input.txt')

    guard_pos = (0, 0)

    for i in range(len(map_area)):
        for j in range(len(map_area[i])):
            if map_area[i][j] == '^':
                guard_pos = (i, j)
                break

    print(guard_pos)

    direction = (-1, 0)

    known_positions = [guard_pos]

    while guard_pos[0] + direction[0] >= 0 and guard_pos[0] + direction[0] < len(map_area) and guard_pos[1] + direction[1] >= 0 and guard_pos[1] + direction[1] < len(map_area[0]):
        guard_pos = (guard_pos[0] + direction[0], guard_pos[1] + direction[1])
        print("Position du garde", guard_pos)
        print("Valeur de la case", map_area[guard_pos[0]][guard_pos[1]])
            
        if map_area[guard_pos[0]][guard_pos[1]] == '#':
            print("Obstacle en", guard_pos)
            guard_pos = (guard_pos[0] - direction[0], guard_pos[1] - direction[1])
            direction = next_direction(direction)
        else:
            if guard_pos not in known_positions:
                known_positions.append(guard_pos)

    print("Part1: ",len(known_positions))
    





