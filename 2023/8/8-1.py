def read_file(filename):
    directions = []
    nodes = {}
    with open(filename, 'r', encoding='utf-8') as file:
        directions = list(file.readline().strip())
        file.readline()
        for line in file:
            node, children = line.split('=')
            nodes[node.strip()] = [child.strip().replace('(', '').replace(')','') for child in children.split(',')]
    directions = [0 if direction == 'L' else 1 for direction in directions]
    return directions, nodes

    
if __name__ == '__main__':
    directions, nodes = read_file('input.txt')
    current_node = 'AAA'
    index = 0
    step = 0
    while current_node != 'ZZZ':
        current_node = nodes[current_node][directions[index]]
        index += 1
        if index >= len(directions):
            index = 0
        step += 1
    print(step)
