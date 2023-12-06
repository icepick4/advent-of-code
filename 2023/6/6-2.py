def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        time = int(file.readline().split(':')[1].replace(' ', ''))
        record = int(file.readline().split(':')[1].replace(' ', ''))
    return time, record

def calculate_distance_travelled(holding_time, total_time):
    if holding_time == 0:
        return 0
    total_time -= holding_time

    return holding_time * total_time
    
if __name__ == '__main__':
    time, to_beat = read_file('input.txt')
    counter = 0
    for i in range(time):
        distance = calculate_distance_travelled(i, time)
        if distance > to_beat:
            counter += 1
    print(counter)
