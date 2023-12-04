def read_file(filename):
    cards = []
    sum = 0
    with open(filename, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            numbers = line.strip().split(':')[1].split('|')
            cards.append([numbers[0].split(' '), numbers[1].split(' ')])
    
    for i in cards:
        sum += count_card_score(i[0], i[1])
    print(sum)

def count_card_score(winning_numbers, numbers):
    score = 0
    winning_numbers_final = []
    for i in range(0, len(winning_numbers)):
        if winning_numbers[i] == '':
            continue
        winning_numbers_final.append(int(winning_numbers[i]))
    for number in numbers:
        if number == '':
            continue
        if int(number) in winning_numbers_final:
            if score == 0:
                score = 1
            else:
                score *= 2
    return score
                
    
if __name__ == '__main__':
    read_file('input.txt')