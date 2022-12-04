def result(weapon1, weapon2):
    if (weapon1 == 'A' and weapon2 == 'X') or (weapon1 == 'B' and weapon2 == 'Y') or (weapon1 == 'C' and weapon2 == 'Z'):
        return 3 + weaponValue(weapon2)
    elif (weapon1 == 'A' and weapon2 == 'Y') or (weapon1 == 'B' and weapon2 == 'Z') or (weapon1 == 'C' and weapon2 == 'X'):
        return 6 + weaponValue(weapon2)
    elif (weapon1 == 'A' and weapon2 == 'Z') or (weapon1 == 'B' and weapon2 == 'X') or (weapon1 == 'C' and weapon2 == 'Y'):
        return 0 + weaponValue(weapon2)


def weaponValue(weapon):
    if weapon == 'X':
        return 1
    elif weapon == 'Y':
        return 2
    elif weapon == 'Z':
        return 3


def read_file(filename):
    tab = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.split(' ')
            if line[1].endswith('\n'):
                line[1] = line[1][:-1]
            tab.append(line)
    return tab


if __name__ == '__main__':
    rounds = read_file('input.txt')
    SUM = 0
    for round in rounds:
        SUM += result(round[0], round[1])
    print(SUM)
