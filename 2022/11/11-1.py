class Monkey:
    def __init__(self, id, items, test, throw):
        self.items = list(items)
        self.test = test
        self.throw_true = throw[0]
        self.throw_false = throw[1]
        self.id = id
        self.counter_inspection = 0

    def receive_item(self, item):
        self.items.append(item)

    def throw_item_to(self, other):
        other.receive_item(self.items.pop(0))

    def operation(self, item):
        if self.id == 0:
            return item*19
        elif self.id == 1:
            return item+8
        elif self.id == 2:
            return item*13
        elif self.id == 3:
            return item+6
        elif self.id == 4:
            return item+5
        elif self.id == 5:
            return item*item
        elif self.id == 6:
            return item+2
        elif self.id == 7:
            return item+3


def read_file(filename):
    tab = []
    with open(filename, 'r') as f:
        throw = [0, 0]
        items = []
        id = -1
        test = -1
        for line in f:
            if line == '\n':
                monkey = Monkey(id, items, test, throw)
                tab.append(monkey)
            if line.strip().endswith(':'):
                id = int(line.strip()[-2])
            elif line.strip().startswith('Starting'):
                items = line.strip().split(':')[1].split(',')
                for i in range(len(items)):
                    items[i] = int(items[i])
            elif line.strip().startswith('Test'):
                test = int(line.strip().split(' ')[-1])
            elif line.strip().startswith('If true'):
                throw[0] = int(line.strip().split(' ')[-1])
            elif line.strip().startswith('If false'):
                throw[1] = int(line.strip().split(' ')[-1])
    return tab


def inspect(monkey, monkeys):
    for _ in range(len(monkey.items)):
        monkey.counter_inspection += 1
        print('monkey', monkey.id, 'inspects item', monkey.items[0])
        monkey.items[0] = monkey.operation(monkey.items[0])
        print('item is now', monkey.items[0])
        monkey.items[0] = monkey.items[0] // 3
        print('item is now', monkey.items[0], 'after divide by 3')
        if monkey.items[0] % monkey.test == 0:
            print('throwing to monkey', monkey.throw_true)
            monkey.throw_item_to(monkeys[monkey.throw_true])
        else:
            print('throwing to monkey', monkey.throw_false)
            monkey.throw_item_to(monkeys[monkey.throw_false])


if __name__ == '__main__':
    monkeys = read_file('input.txt')
    for _ in range(20):
        for monkey in monkeys:
            if monkey.items != []:
                inspect(monkey, monkeys)
    for monkey in monkeys:
        print(monkey.counter_inspection)
