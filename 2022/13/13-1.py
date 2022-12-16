import json


def read_file(filename):
    tab = []
    with open(filename, 'r') as f:
        for line in f:
            if line == '\n':
                continue
            line = json.loads(line)
            tab.append(line)
    return tab


def compare_pairs(pair1, pair2):
    pass


def compare_lists(left_list, right_list):
    for i in range(len(left_list)):
        try:
            if left_list[i] < right_list[i]:
                return True
            elif left_list[i] > right_list[i]:
                return False
        except IndexError:
            return False
    try:
        right_list[i] = None
    except IndexError:
        return True

    return None


def compare_integers(left, right):
    return None if left == right else left < right


if __name__ == '__main__':
    tab = read_file('input-test.txt')
    print(tab)
