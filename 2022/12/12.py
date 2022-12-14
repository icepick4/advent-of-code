from math import inf


def read_file(filename):
    tab = []
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            tab.append([])
            for j, char in enumerate(line.strip()):
                tab[i].append(char)
                if char == 'S':
                    start_pos = [i, j]
                elif char == 'E':
                    end_pos = [i, j]
    return tab, start_pos, end_pos


def dijkstra(graphe, start, end):
    # all nodes are not visited
    visited = {s: False for s in graphe}
    # the distance from the start to each node is infinite
    distance = {s: (inf, None) for s in graphe}
    distance[start] = (0, None)
    file = [(0, start)]
    while file:
        current_pos = min(file)
        file.remove(current_pos)
        current_dist, current_node = current_pos
        # if the current not is not visited check if it is the end
        if not visited[current_node]:
            if current_node == end:
                break
            # set the current node as visited
            visited[current_node] = False
            # for each neighbor of the current node
            for A, neighbor in graphe[current_node]:
                # if the neighbor is not visited, check new distance
                if not visited[neighbor]:
                    new_distance = current_dist+A
                    if new_distance < distance[neighbor][0]:
                        distance[neighbor] = (new_distance, current_node)
                        file.append((new_distance, neighbor))
    # return the distance from the start to the end
    return distance[end][0]


if __name__ == '__main__':
    tab, start, end = read_file('input.txt')
    tab[start[0]][start[1]] = 'a'
    tab[end[0]][end[1]] = 'z'
    graphe = {}
    for i, line in enumerate(tab):
        for j, char in enumerate(line):
            graphe[i, j] = []
            # if the neighbor is the next letter or the same, add an edge of weight 1
            if i > 0 and ord(tab[i - 1][j]) - ord(char) <= 1:
                graphe[i, j].append((1, (i-1, j)))
            if i < len(tab) - 1 and ord(tab[i + 1][j]) - ord(char) <= 1:
                graphe[i, j].append((1, (i+1, j)))
            if j > 0 and ord(tab[i][j - 1]) - ord(char) <= 1:
                graphe[i, j].append((1, (i, j-1)))
            if j < len(line) - 1 and ord(tab[i][j + 1]) - ord(char) <= 1:
                graphe[i, j].append((1, (i, j+1)))
    # PART 1
    print('Going from', start, 'to', end, 'in')
    print('length of that path is : ', dijkstra(
        graphe, (start[0], start[1]), (end[0], end[1])))
    # PART 2
    paths = []
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if (tab[i][j]) == 'a':
                start = [i, j]
                paths.append(
                    dijkstra(graphe, (start[0], start[1]), (end[0], end[1])))
    print('the shortest path is : ', min(paths))
