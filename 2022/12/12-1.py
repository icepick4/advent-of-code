def read_file(filename):
    tab = []
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            tab.append([])
            for j, char in enumerate(line.strip()):
                tab[i].append(char)
                if char == 'S':
                    start_pos = [i, j]
                elif char == 'E':
                    end_pos = [i, j]
    return tab, start_pos, end_pos


def move(tab, current, visited):
    i, j = current
    # up
    if i > 0:
        if ord(tab[i-1][j]) == ord(tab[i][j]) + 1:
            print('NEXT LETTER', tab[i-1][j], 'on position', [i-1, j])
            return [i-1, j]
    # down
    if i < len(tab) - 1:
        if ord(tab[i+1][j]) == ord(tab[i][j]) + 1:
            print('NEXT LETTER', tab[i+1][j], 'on position', [i+1, j])
            return [i+1, j]
    # left
    if j > 0:
        if ord(tab[i][j-1]) == ord(tab[i][j]) + 1:
            print('NEXT LETTER', tab[i][j-1], 'on position', [i, j-1])
            return [i, j-1]
    # right
    if j < len(tab[i]) - 1:
        if ord(tab[i][j+1]) == ord(tab[i][j]) + 1:
            print('NEXT LETTER', tab[i][j+1], 'on position', [i, j+1])
            return [i, j+1]
    # now check if we can move to the same letter
    # down
    if i < len(tab) - 1:
        if ord(tab[i+1][j]) == ord(tab[i][j]) and [i+1, j] not in visited:
            print('Moving to the same letter',
                  tab[i+1][j], 'on position', [i+1, j])
            return [i+1, j]
    # up
    if i > 0:
        if ord(tab[i-1][j]) == ord(tab[i][j]) and [i-1, j] not in visited:
            print('Moving to the same letter',
                  tab[i-1][j], 'on position', [i-1, j])
            return [i-1, j]
    # left
    if j > 0:
        if ord(tab[i][j-1]) == ord(tab[i][j]) and [i, j-1] not in visited:
            print('Moving to the same letter',
                  tab[i][j-1], 'on position', [i, j-1])
            return [i, j-1]
    # right
    if j < len(tab[i]) - 1:
        if ord(tab[i][j+1]) == ord(tab[i][j]) and [i, j+1] not in visited:
            print('Moving to the same letter',
                  tab[i][j+1], 'on position', [i, j+1])
            return [i, j+1]
    # for i, row in enumerate(tab):
    #     for j, char in enumerate(row):
    #         if char == 'E':
    #             return [i, j]


if __name__ == '__main__':
    tab, start, end = read_file('input.txt')
    current = start
    tab[start[0]][start[1]] = 'a'
    counter = 0
    print(end, start)
    visited = [start]
    while current != end:
        current = move(tab, current, visited)
        visited.append(current)
        counter += 1
        print('Current position:', current)
        print()
    print('Number of moves:', counter)
