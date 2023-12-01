import re

def read_file(filename):
    sum = 0
    numbers = ['one','two','three','four','five','six','seven','eight','nine']
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            matches = re.findall("(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)
            print(matches)
            if len(matches) == 1:
                matches.append(matches[0])
            if not matches[0].isdigit():
                matches[0] = str(numbers.index(matches[0]) +1)
            if not matches[len(matches) -1].isdigit():
                matches[len(matches) -1] = str(numbers.index(matches[len(matches) -1]) +1)
            print(int(matches[0] + matches[len(matches) -1]))
            sum += int(matches[0] + matches[len(matches) -1])
    print(sum)

if __name__ == '__main__':
    read_file('input.txt')