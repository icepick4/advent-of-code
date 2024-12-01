def read_file(file_name):
    grid = []
    with open(file_name, 'r') as file:
        for line in file:
            line = list(line.strip())
            grid.append(line)
            if 'S' in line:
                start = (grid.index(line), line.index('S'))
    return grid, start


def find_directions(previous_direction, point, grid):
    pipes = {
        '|': ((-1, 0), (1, 0)),
        '-': ((0, -1), (0, 1)),
        'J': ((-1, 0), (0, -1)),
        'L': ((-1, 0), (0, 1)),
        '7': ((1, 0), (0, -1)),
        'F': ((1, 0), (0, 1))
    }
    for pipe in pipes:
        if pipe in grid[point[0]][point[1]]:
            for direction in pipes[pipe]:
                direction = (direction[0]+point[0], direction[1]+point[1])
                if direction != previous_direction:
                    return direction


def find_start(starting_point, grid):
    directions = [(0,1),(1,0), (0,-1), (-1,0)]
    for direction in directions:
        point = (starting_point[0]+direction[0], starting_point[1]+direction[1])
        connections = find_directions(None, point, grid)
        if starting_point in connections:
            return point
        


if __name__ == '__main__':
    grid, start = read_file('input-test.txt')
    print('starting point : ', start)
    for line in grid:
        print("".join(line))
    print(find_directions((1,3), grid))
    # print(find_start(start, grid))
    


    