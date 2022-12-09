def read_file(filename):
    tab = []
    with open(filename, 'r') as f:
        for line in f:
            temp = line.strip().split(' ')
            tab.append([temp[0], int(temp[1])])
    return tab


class Head:
    def __init__(self):
        self.position = [0, 0]

    def move(self, direction):
        self.position[0] += direction[0]
        self.position[1] += direction[1]


class Tail:
    def __init__(self):
        self.position = [0, 0]

    def get_position(self):
        return self.position

    def is_adjecent(self, head):
        if head.position[0] == self.position[0] and abs(head.position[1] - self.position[1]) == 1:
            return True
        elif head.position[1] == self.position[1] and abs(head.position[0] - self.position[0]) == 1:
            return True
        elif abs(head.position[0] - self.position[0]) == 1 and abs(head.position[1] - self.position[1]) == 1:
            return True
        else:
            return False

    def follow(self, head):
        if head.position[0] > self.position[0]:
            self.position[0] += 1
        elif head.position[0] < self.position[0]:
            self.position[0] -= 1
        if head.position[1] > self.position[1]:
            self.position[1] += 1
        elif head.position[1] < self.position[1]:
            self.position[1] -= 1


if __name__ == '__main__':
    actions = read_file('input-test.txt')
    values = {
        'U': [0, -1],
        'L': [-1, 0],
        'D': [0, 1],
        'R': [1, 0]
    }
    positions = [[0, 0]]
    head = Head()
    tail = Tail()
    all_pos = []
    for action in actions:
        # print(action)
        for _ in range(action[1]):
            head.move(values[action[0]])
            pos_x, pos_y = tail.get_position()[0], tail.get_position()[1]
            # print(pos_x, pos_y)
            # print(head.position)
            if [pos_x, pos_y] not in positions:
                positions.append([pos_x, pos_y])
            all_pos.append([pos_x, pos_y])
            if not tail.is_adjecent(head):
                tail.follow(head)
    print(positions)
    print(len(positions))
