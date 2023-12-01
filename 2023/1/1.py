import re

def read_file(filename):
    sum = 0
    regex = '\d'
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            matches = re.findall(regex, line)
            if len(matches) == 1:
                matches.append(matches[0])
            sum += int(matches[0] + matches[len(matches) -1])
    print(sum)

if __name__ == '__main__':
    read_file('input.txt')