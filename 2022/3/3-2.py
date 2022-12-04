

def read_file(filename):
    tab = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if line.endswith('\n'):
                line = line[:-1]
            tab.append(line)
    return tab


def findCommon(compartment1, compartment2, compartment3):
    for letter in compartment1:
        if letter in compartment2 and letter in compartment3:
            return letter
    return 'NO LETTER IN COMMON'


def letterValue(letter):
    value = ord(letter)
    return value - 38 if value <= 90 else value - 96


if __name__ == '__main__':
    compartments = read_file('input.txt')
    SUM = 0
    for i in range(0, len(compartments), 3):
        letter = findCommon(
            compartments[i], compartments[i+1], compartments[i+2])
        SUM += letterValue(letter)
    print(SUM)
