def read_file(filename):
    rules = []
    updates_printing = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if line == '\n':
                break
            rules.append(line.strip().split('|'))
        for line in file:
            updates_printing.append(line.strip().split(','))

    rules = [ [int(rule[i]) for i in range(len(rule))] for rule in rules]

    updates_printing = [ [int(update[i]) for i in range(len(update))] for update in updates_printing]

    return rules, updates_printing


def replace_update(rule, update):
    index = update.index(rule[0])
    update[index] = rule[1]
    
    index = update.index(rule[1])
    update[index] = rule[0]

    return update

def is_valid_update(rule, update):
    if rule[0] in update:
        index = update.index(rule[0])
        if rule[1] in update[:index]:
            return False
    return True

if __name__ == '__main__':
    rules, updates_printing = read_file('input.txt')

    somme = 0
    somme2 = 0

    broken_updates = []

    for i in range(len(updates_printing)):
        middle_update = updates_printing[i][len(updates_printing[i])//2]
        valid_update = True
        for j in range(len(rules)):
            if not is_valid_update(rules[j], updates_printing[i]):
                valid_update = False
                broken_updates.append(updates_printing[i])
                break
        if valid_update:
            somme += middle_update

    for i in range(len(broken_updates)):
        all_rules_valid = False
        while not all_rules_valid:
            all_rules_valid = True
            for j in range(len(rules)):
                if not is_valid_update(rules[j], broken_updates[i]):
                    all_rules_valid = False
                    broken_updates[i] = replace_update(rules[j], broken_updates[i])
                    break
        middle_update = broken_updates[i][len(broken_updates[i])//2]
        somme2 += middle_update

    print("Part1", somme)
    print("Part2", somme2)



