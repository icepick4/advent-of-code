def read_file(filename):
    hands = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            hand, bid = line.split()
            hands.append({'cards': list(hand), 'bid': int(bid)})
    return hands

def calculate_hand_score(hand):
    score = 0
    if is_five_of_a_kind(hand):
        # print('hand', hand, 'is five of a kind')
        score += 7
    elif is_four_of_a_kind(hand):
        # print('hand', hand, 'is four of a kind')
        score += 6
    elif is_full_house(hand):
        # print('hand', hand, 'is full house')
        score += 5
    elif is_three_of_a_kind(hand):
        # print('hand', hand, 'is three of a kind')
        score += 4
    elif is_two_pairs(hand):
        # print('hand', hand, 'is two pairs')
        score += 3
    elif is_one_pair(hand):
        # print('hand', hand, 'is one pair')
        score += 2
    else:
        # print('hand', hand, 'is high card')
        score += 1
    return score

def is_five_of_a_kind(hand):
    if hand.count('J') == 5:
        return True
    for value in hand:
        if hand.count(value) + hand.count('J') == 5:
            return True
    return False

def is_four_of_a_kind(hand):
    if hand.count('J') == 4:
        return True
    for value in hand:
        if hand.count(value) + hand.count('J') == 4 and value != 'J':
            return True
    return False
    

def is_full_house(hand):

    for value in hand:
        joker_count = hand.count('J')
        if hand.count(value) + joker_count == 3:
            joker_count = 0
            first_value = value
            for value in hand:
                if hand.count(value) == 2 and value != first_value and value != 'J':
                    return True
    return False


def is_three_of_a_kind(hand):
    if hand.count('J') == 3:
        return True
    for value in hand:
        if hand.count(value) + hand.count('J') == 3:
            return True
    return False

def is_two_pairs(hand):
    pairs = 0
    first_pair = ''
    for value in hand:
        if hand.count(value) == 2 and value != first_pair:
            pairs += 1
            if first_pair == '':
                first_pair = value
            elif first_pair != value:
                return True
    return pairs == 2

def is_one_pair(hand):
    for value in hand:
        if hand.count(value) == 2:
            return True
    if hand.count('J') == 1:
        return True
    return False


def compare_card_value_hands(hand1, hand2):
    rules = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14}

    for card1, card2 in zip(hand1, hand2):
        if rules[card1] > rules[card2]:
            return hand1
        elif rules[card1] < rules[card2]:
            return hand2
    return None


    
if __name__ == '__main__':
    hands = read_file('input.txt')
    for i, hand in enumerate(hands):
        hand['score'] = calculate_hand_score(hand['cards'])
    hands = sorted(hands, key=lambda x: x['score'])
    for i in range(len(hands)):
        for j in range(i+1, len(hands)):
            if hands[i]['score'] == hands[j]['score']:
                winner = compare_card_value_hands(hands[i]['cards'], hands[j]['cards'])
                if winner == hands[i]['cards']:
                    hands[i], hands[j] = hands[j], hands[i]
    total_winnings = 0
    for i, hand in enumerate(hands):
        score = hand['bid'] * (i+1)
        total_winnings += score
    print(total_winnings)
