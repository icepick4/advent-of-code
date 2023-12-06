def read_file(filename):
    races = {}
    with open(filename, 'r', encoding='utf-8') as file:
        times = file.readline().split(':')[1].split(' ')
        records = file.readline().split(':')[1].split(' ')
        times = [int(x) for x in times if x != '']
        records = [int(x) for x in records if x != '']
        for i, time in enumerate(times):
            races[time] = records[i]
    return races

def calculate_distance_travelled(holding_time, total_time):
    if holding_time == 0:
        return 0
    total_time -= holding_time

    return holding_time * total_time
    
if __name__ == '__main__':
    races = read_file('input.txt')
    result = 1
    for time, to_beat in races.items():
        counter = 0
        for i in range(time):
            distance = calculate_distance_travelled(i, time)
            if distance > to_beat:
                counter += 1
        result *= counter
    print(result)
