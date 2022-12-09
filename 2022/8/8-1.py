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
    SUM = 0
    SUM += len(arbres) * 2 + (len(arbres[0]) - 2) * 2
    for i in range(1, len(arbres) - 1):
        for j in range(1, len(arbres[i]) - 1):
            top = True
            bot = True
            left = True
            right = True
            for k in range(0, i):
                if arbres[k][j] >= arbres[i][j]:
                    top = False
                    break
            for k in range(0, j):
                if arbres[i][j - k] >= arbres[i][j]:
                    left = False
                    break
            for k in range(i + 1, len(arbres)):
                if arbres[k][j] >= arbres[i][j]:
                    bot = False
                    break
            for k in range(j + 1, len(arbres[0])):
                if arbres[i][k] >= arbres[i][j]:
                    right = False
                    break
            print(i, j)
            if top:
                print('visible depuis le haut')
            elif bot:
                print('visible depuis le bas')
            elif left:
                print('visible depuis la gauche')
            elif right:
                print('visible depuis la droite')
            else:
                print('pas visible')

            if top or bot or left or right:
                SUM += 1
    print(SUM)
