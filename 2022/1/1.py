def read_file(filename):
    tab = []
    with open(filename, 'r', encoding='utf-8') as f:
        elve = 0
        number = ''
        for line in f:
            for num in line:
                if num != '\n':
                    number += num
            try:
                elve += int(number)
            except ValueError:
                tab.append(elve)
                elve = 0
            number = ''
    return tab


if __name__ == '__main__':
    elves = read_file('input.txt')
    top1 = max(elves)
    elves.remove(max(elves))
    top2 = max(elves)
    elves.remove(max(elves))
    top3 = max(elves)
    elves.remove(max(elves))
    print(top1, top2, top3)
    print(top1+top2+top3)
