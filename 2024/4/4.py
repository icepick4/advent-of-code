def read_file(filename):
    word_search = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            word_search.append(line.strip())
    return word_search

def search_case(i,j,table):
    xmas = "XMAS"

    directions = [(0,1), (1,0), (1,1), (1,-1), (-1,1), (-1,-1), (0,-1), (-1,0)]

    xmas_count = 0
    
    for direction in directions:
        for position in range(len(xmas)):
            if 0 <= i + position*direction[0] < len(table) and 0 <= j + position*direction[1] < len(table[i]):
                if table[i + position*direction[0]][j + position*direction[1]] != xmas[position]:
                    break
            else:
                break
        else:
            print("XMAS found at position: ", i, j)
            print("Direction: ", direction)
            xmas_count += 1

    return xmas_count

def search_case_mas(i,j,table):
    if table[i][j] != 'A':
        return False
    
    if i < 1 or j < 1 or i+1 >= len(table) or j+1 >= len(table[i]):
        return False
    
    first_diag = False
    second_diag = False
    
    if (table[i-1][j-1] == "M" and table[i+1][j+1] == "S") or (table[i-1][j-1] == "S" and table[i+1][j+1] == "M"):
        first_diag = True
    if (table[i-1][j+1] == "M" and table[i+1][j-1] == "S") or (table[i-1][j+1] == "S" and table[i+1][j-1] == "M"):
        second_diag = True

    return first_diag and second_diag


if __name__ == '__main__':
    word_search = read_file('input.txt')

    xmas_count = 0
    x_mas_count = 0

    print(word_search)
    print(len(word_search))

    for i in range(len(word_search)):
        for j in range(len(word_search[i])):
            if word_search[i][j] == "X":
                xmas_count += search_case(i,j,word_search)
            x_mas_count += search_case_mas(i,j,word_search)

    print("Part1:",xmas_count)
    print("Part2:",x_mas_count)