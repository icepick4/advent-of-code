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


def move(tab, current):
    pass


if __name__ == '__main__':
    tab, start, end = read_file('input-test.txt')
    current = start
    while current != end:
        pass
