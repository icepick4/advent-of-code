class Pile:

    """Implémentation d'une Pile à l'aide d'une Liste"""

    def __init__(self):
        # Initialiser une pile vide (libre)
        self.pile = []

    def empiler(self, element):
        return self.pile.append(element)

    def depiler(self):
        return self.pile.pop()

    def reverse(self):
        """Retourner la Pile à l'envers"""
        self.pile = self.pile[::-1]
        return self

    def pile_vide(self):
        """Retourner Vrai si la pile est vide, sinon Faux"""
        if self.pile == []:
            return True
        else:
            return False

    def __str__(self):
        for i in self.pile:
            print(i, end=' ')
        return ''


def read_file(filename):
    tab = []
    stacks = []
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i in range(len(lines[0])//4):
            stacks.append(Pile())
        j = 0
        k = 0
        while lines[j] != '\n':
            while lines[j][k] != '\n':
                if lines[j][k] == '[':
                    # print('J\'empile ', lines[j][k+1], ' dans la pile ', k//4)
                    stacks[k//4].empiler(lines[j][k+1])
                k += 1
            j += 1
            k = 0
        for line in lines[j+1:]:
            temp = []
            for ctr, char in enumerate(line):
                if char.isdigit() and not line[ctr - 1].isdigit():
                    try:
                        if line[ctr+1].isdigit():
                            temp.append(int(char+line[ctr+1]))
                            two_digits = True
                        else:
                            temp.append(int(char))
                    except IndexError:
                        temp.append(int(char))
            tab.append(temp)

    return stacks, tab


if __name__ == '__main__':
    stacks, tab = read_file('input.txt')
    for i in range(len(stacks)):
        stacks[i] = stacks[i].reverse()
    ctr = 0
    for infos in tab:
        print('Je dépile ', infos[0], 'fois depuis la pile ',
              infos[1], 'dans la pile ', infos[2])
        print('La pile de départ : ')
        print(stacks[infos[1] - 1])
        print('La pile d arrivée : ')
        print(stacks[infos[2] - 1])
        valuesToMoves = []
        for i in range(infos[0]):
            valuesToMoves.append(stacks[infos[1] - 1].depiler())
        # valuesToMoves = valuesToMoves[::-1] <- keep same order
        for value in valuesToMoves:
            stacks[infos[2] - 1].empiler(value)
        print('La pile de départ : ')
        print(stacks[infos[1] - 1])
        print('La pile d arrivée : ')
        print(stacks[infos[2] - 1])
        print('-----------------------')
    for i in stacks:
        print(i.depiler(), end='')
