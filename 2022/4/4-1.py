

def read_file(filename):
    tab = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if line.endswith('\n'):
                line = line[:-1]
            line = line.split(',')
            line[0] = line[0].split('-')
            line[1] = line[1].split('-')
            j = 0
            for i, pair in enumerate(line):
                for number in pair:
                    line[i][j] = int(number)
                    j += 1
                j = 0
            tab.append(line)
    return tab


def fullyContains(firstSet, secondSet):
    """return true if firstSet fully contains seconde one"""
    return secondSet[0] >= firstSet[0] and secondSet[1] <= firstSet[1]


if __name__ == '__main__':
    pairs = read_file('input.txt')
    COUNTER = 0
    for pair in pairs:
        if fullyContains(pair[0], pair[1]) or fullyContains(pair[1], pair[0]):
            COUNTER += 1

    print(COUNTER)
