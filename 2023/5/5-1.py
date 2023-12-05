import re


def read_file(filename):
    seeds = []
    maps = []
    with open(filename, 'r', encoding='utf-8') as file:
        line = file.readline()
        line = line.split(':')[1].split(' ')
        for i in range(0, len(line)):
            if line[i] == '':
                continue
            seeds.append(int(line[i]))
        for line in file:
            line = re.sub('[a-zA-Z-]', '', line).strip()
            maps.append(line.split(':'))
    mapped_values = []
    for i, map in enumerate(maps):
        if '' in map:
            mapped_values.append([])
            continue
        mapped_values[-1].append(tuple([int(x) for x in map[0].split(' ')]))

    mapped_values = [x for x in mapped_values if x != []]
    return mapped_values, seeds


    
if __name__ == '__main__':
    maps, seeds = read_file('input.txt')
    for map in maps:
        result = []
        for seed in seeds:
            for destination, source, range in map:
                if seed >= source and seed <= source + range:
                    seed = destination + seed - source
                    break
            result.append(seed)
        final_seeds = result
    print(min(final_seeds))