def read_file(filename):
    tab = []
    with open(filename, 'r') as f:
        for line in f:
            temp = int(line.strip().split(' ')[
                       1]) if line.startswith('add') else None
            tab.append(temp)
    return tab


def check_cycle(cycle):
    return cycle % 40 == 0 and cycle != 0


def empty_line():
    return ['.' for _ in range(40)]


def check_register(register, cycle):
    return register - 1 == cycle % 40 or register + 1 == cycle % 40 or register == cycle % 40


if __name__ == '__main__':
    actions = read_file('input.txt')
    CYCLE = 0
    REGISTER = 1
    crt = [empty_line()]
    current_line = 0
    for action in actions:
        if check_cycle(CYCLE):
            crt.append(empty_line())
            current_line += 1
        if check_register(REGISTER, CYCLE):
            crt[current_line][CYCLE % 40] = '#'
        CYCLE += 1
        if action is not None:
            if check_cycle(CYCLE):
                crt.append(empty_line())
                current_line += 1
            if check_register(REGISTER, CYCLE):
                crt[current_line][CYCLE % 40] = '#'
            CYCLE += 1
            REGISTER += action
    for line in crt:
        for char in line:
            print(char, end=' ')
        print('\n')
    print(len(crt))
