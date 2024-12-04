import re


def read_file(filename):
    mul = ""
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            mul += line
    return mul


if __name__ == '__main__':
    mul = read_file('input.txt')

    while "don't()" in mul:
        index_dont = mul.index("don't()")

        index_do = mul.index("do()", index_dont)

        mul = mul[:index_dont] + mul[index_do + 4:]
        

    regex = r"mul\((\d+),(\d+)\)"

    matches = re.finditer(regex, mul)

    somme = 0

    for match in matches:
        # print(match.group(1), match.group(2))
        # print(int(match.group(1)) * int(match.group(2)))
        somme += int(match.group(1)) * int(match.group(2))

    print(somme)
    # print(mul)