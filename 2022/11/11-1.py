class Monkey:
    def __init__(self, items, operation, test, throw):
        self.items = list(items)
        self.operation = operation
        self.test = test
        self.throw = list(throw)

    def receive_item(self, item):
        self.items.append(item)

    def throw_item_to(self, other):
        other.receive_item(self.items.pop())


def read_file(filename):
    tab = []
    with open(filename, 'r') as f:
        for line in f:
            if line == '\n':
                tab.append(monkey)
                monkey = []
            if line.startswith('Starting'):
                items = line.strip().split(',')
            elif line.startswith('Operation'):
                operation = line.strip().split('old')[1]
                if operation == '*':
                    def operation(x): return x*operation[1]
    return tab


if __name__ == '__main__':
    monkeys = read_file('input-test.txt')
