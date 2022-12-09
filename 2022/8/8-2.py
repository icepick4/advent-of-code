def read_file(filename):
    tab = []
    with open(filename, 'r') as f:
        for line in f:
            arbres = line.strip()
            temp = []
            for arbre in arbres:
                temp.append(int(arbre))
            tab.append(temp)
    return tab


if __name__ == '__main__':
    arbres = read_file('input.txt')
    MAXI = 0
    for i in range(1, len(arbres) - 1):
        for j in range(1, len(arbres[i]) - 1):
            top = 0
            bot = 0
            left = 0
            right = 0
            for k in range(i):
                top += 1
                if arbres[i - 1 - k][j] >= arbres[i][j]:
                    break
            for k in range(j):
                left += 1
                if arbres[i][j - 1 - k] >= arbres[i][j]:
                    break
            for k in range(i + 1, len(arbres)):
                bot += 1
                if arbres[k][j] >= arbres[i][j]:
                    break
            for k in range(j + 1, len(arbres[0])):
                right += 1
                if arbres[i][k] >= arbres[i][j]:
                    break
            print(i, j)
            print(top, left, bot, right)
            scenic_score = top * bot * left * right
            if scenic_score > MAXI:
                MAXI = scenic_score
    print(MAXI)
