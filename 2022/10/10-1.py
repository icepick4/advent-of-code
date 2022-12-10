def read_file(filename):
    tab = []
    with open(filename, 'r') as f:
        for line in f:
            temp = int(line.strip().split(' ')[
                       1]) if line.startswith('add') else None
            tab.append(temp)
    return tab


def check_cycle(cycle):
    return cycle % 40 == 20


if __name__ == '__main__':
    actions = read_file('input.txt')
    CYCLE = 0
    SUM = 0
    REGISTER = 1
    for action in actions:
        CYCLE += 1
        if check_cycle(CYCLE):
            SUM += REGISTER * CYCLE
        if action is not None:
            CYCLE += 1
            if check_cycle(CYCLE):
                SUM += REGISTER * CYCLE
            REGISTER += action
    print(SUM)
