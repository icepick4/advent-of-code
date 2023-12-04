def read_file(filename):
    cards = []
    cards_occurences = []
    with open(filename, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            numbers = line.strip().split(':')[1].split('|')
            cards.append([numbers[0].split(' '), numbers[1].split(' ')])
    
    for i in cards:
        cards_occurences.append(1)
    for i, card in enumerate(cards):
        for _ in range(cards_occurences[i]):
            current_score = count_card_score(card[0], card[1])
            for j in range(current_score):
                cards_occurences[i + j + 1] += 1
    print(sum(cards_occurences))

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
            score += 1
    return score
                
    
if __name__ == '__main__':
    read_file('input.txt')