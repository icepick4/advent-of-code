def read_file(filename):
    sum = 0
    with open(filename, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            sets = line.split(':')[1].split(';')
            highest_red = 1
            highest_green = 1
            highest_blue = 1
            for set in sets:
                for pair in set.split(','):
                    count, color = pair.strip().split(' ')
                    count = int(count)
                    if color == 'red' and highest_red < count:
                        highest_red = count
                    elif color == 'green' and highest_green < count:
                        highest_green = count
                    elif color == 'blue' and highest_blue < count:
                        highest_blue = count
            result = highest_blue * highest_green * highest_red
            sum += result
    print(sum)

if __name__ == '__main__':
    read_file('input.txt')