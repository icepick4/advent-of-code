from itertools import product


def read_file(filename):
    equations = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            equations.append(line.strip())

    return equations

def test_operators(equation):
    res = 0

    return None

def operators_order_possibilities(operators, possible_operators):
    combinations = list(product(operators, repeat=possible_operators))

    return combinations

def concatenation(left, right):
    return int(str(left) + str(right))

if __name__ == '__main__':
    equations = read_file('input.txt')
    global_somme = 0
    operators = ['+', '*']
    for equation in equations:
        res, equation = equation.split(':')
        res = int(res)
        equation = equation.strip().split(' ')
        equation = [int(number) if number.isdigit() else number for number in equation]
        print(equation)
        possible_operators = len(equation) - 1
        
        operator_combinations = operators_order_possibilities(operators, possible_operators)

        # print(operator_combinations) 
        for operator_combination in operator_combinations:
            somme = equation[0]
            for i, number in enumerate(equation[1:]):
                # print(i, number)
                if operator_combination[i].startswith('+'):
                    somme += number
                elif operator_combination[i].startswith('*'):
                    somme *= number
            # print(somme)
            if somme == res:
                global_somme += somme
                break

    print("Part1: ", global_somme)
                
    