def read_file(filename):
    colors = {'red': 12, 'green': 13, 'blue': 14}
    not_possible_ids = []
    with open(filename, 'r', encoding='utf-8') as file:
        number_of_lines = 0
        for i, line in enumerate(file):
            game_id = i + 1
            sets = line.split(':')[1].split(';')
            for set in sets:
                for pair in set.split(','):
                    count, color = pair.strip().split(' ')
                    if colors[color] < int(count) and game_id not in not_possible_ids:
                        not_possible_ids.append(game_id)
            number_of_lines += 1
    result = 0
    for i in range(1, number_of_lines + 1):
        if i not in not_possible_ids:
            result += i
    print(result)

if __name__ == '__main__':
    read_file('input.txt')