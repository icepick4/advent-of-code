def read_file(filename):
    right = []
    left = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            couple = line.split(' ')
            left.append(int(couple[0]))
            right.append(int(couple[len(couple) - 1].strip()))
    
    return left, right

if __name__ == '__main__':
    left, right = read_file('input.txt')
    somme = 0
    for i in range(len(left)):
        min_left = min(left)
        min_right = min(right)
        distance = abs(min_left - min_right)
        somme += distance
        left.remove(min_left)
        right.remove(min_right)

    print("Part1: ", somme)

    left, right = read_file('input.txt')
    somme = 0

    for i in range(len(left)):
        current_left = left[i]

        count_right = right.count(current_left)
        print(count_right)
        somme += (count_right * current_left)

    print("Part2: ",somme)