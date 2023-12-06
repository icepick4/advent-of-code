import re

def read_file(filename):
    seed_ranges = []
    maps = []
    with open(filename, 'r', encoding='utf-8') as file:
        line = file.readline()
        line = line.split(':')[1].split()
        for i in range(0, len(line), 2):
            start = int(line[i])
            length = int(line[i+1])
            seed_ranges.append(range(start, start+length))
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
    return mapped_values, seed_ranges

def apply_mapping(seed, mapping):
    for destination, source, length in mapping:
        if seed >= source and seed < source + length:
            return destination + seed - source
    return seed
    
if __name__ == '__main__':
    maps, seed_ranges = read_file('input.txt')
    result = set()
    for seed_range in seed_ranges[2:]:
        for seed in seed_range:
            percentage = (seed - seed_range.start) / (seed_range.stop - seed_range.start) * 100
            for mapping in maps:
                seed = apply_mapping(seed, mapping)
            result.add(seed)
        print(min(result))
    print(min(result))