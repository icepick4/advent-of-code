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
        self.last_position = [0, 0]
        self.name = 'tail'

    def get_position(self):
        return self.position

    def is_adjecent(self, head):
        if head.position[0] == self.position[0] and abs(head.position[1] - self.position[1]) == 1:
            return True
        elif head.position[1] == self.position[1] and abs(head.position[0] - self.position[0]) == 1:
            return True
        elif abs(head.position[0] - self.position[0]) == 1 and abs(head.position[1] - self.position[1]) == 1:
            return True
        elif head.position[0] == self.position[0] and head.position[1] == self.position[1]:
            return True
        return False

    def follow(self, head):
        self.last_position = self.position
        if head.position[0] > self.position[0]:
            self.position[0] += 1
        elif head.position[0] < self.position[0]:
            self.position[0] -= 1
        if head.position[1] > self.position[1]:
            self.position[1] += 1
        elif head.position[1] < self.position[1]:
            self.position[1] -= 1


if __name__ == '__main__':
    actions = read_file('input.txt')
    values = {
        'U': [0, -1],
        'L': [-1, 0],
        'D': [0, 1],
        'R': [1, 0]
    }
    positions = [[0, 0]]
    head = Head()
    tails = [Tail() for _ in range(9)]
    tails[0].name = 'tail0'
    tails[len(tails)-1].name = 'real tail'
    for action in actions:
        for _ in range(action[1]):
            head.move(values[action[0]])
            # move the first tail (the one that follows the head)
            if not tails[len(tails)-1].is_adjecent(head):
                tails[len(tails)-1].follow(head)
            # move the other tails
            for i in range(len(tails)-1, 0, -1):
                if not tails[i-1].is_adjecent(tails[i]):
                    tails[i-1].follow(tails[i])
            pos_x, pos_y = tails[0].get_position(
            )[0], tails[0].get_position()[1]
            if [pos_x, pos_y] not in positions:
                positions.append([pos_x, pos_y])
        print('--------')
        for tail in tails:
            print(tail.position)

    print(len(positions))
