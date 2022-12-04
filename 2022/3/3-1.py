

def read_file(filename):
    tab = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if line.endswith('\n'):
                line = line[:-1]
            firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
            tab.append([firstpart, secondpart])
    return tab


def findCommon(compartment):
    for letter in compartment[0]:
        if letter in compartment[1]:
            return letter
    return 'NO LETTER IN COMMON'


def letterValue(letter):
    value = ord(letter)
    return value - 38 if value <= 90 else value - 96


if __name__ == '__main__':
    compartments = read_file('input.txt')
    SUM = 0
    for compartment in compartments:
        letter = findCommon(compartment)
        SUM += letterValue(letter)

    print(SUM)
