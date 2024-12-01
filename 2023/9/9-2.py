def read_file(filename):
    histories = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            histories.append([int(value) for value in line.strip().split(' ')])
    return histories


def find_lists(history):
    lists = [history]
    current_list = history
    while not all([value == 0 for value in current_list]):
        list_to_add = []
        for i in range(len(current_list)-1):
            list_to_add.append(current_list[i + 1] - current_list[i])
        lists.append(list_to_add)
        current_list = list_to_add
    return lists


def find_next(lists):
    for i in range(len(lists)-1, 0, -1):
        # print('adding', lists[i-1][len(lists[i-1])-1] + lists[i][len(lists[i])-1], 'into', lists[i-1])
        lists[i-1].append(lists[i-1][len(lists[i-1])-1] + lists[i][len(lists[i])-1])
    return lists[0][-1]


def find_previous(lists):
    for i in range(len(lists)-1, 0, -1):
        print('adding', lists[i-1][0] - lists[i][0], 'into', lists[i-1])
        lists[i-1].insert(0, lists[i-1][0] - lists[i][0])
    return lists[0][0]


if __name__ == '__main__':
    histories = read_file('input.txt')
    sum = 0
    for history in histories:
        lists = find_lists(history)
        sum += find_previous(lists)
    print(sum)