def read_file(filename):
    string = ''
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            string += line
    return string


if __name__ == '__main__':
    string = read_file('input.txt')
    for i in range(4, len(string)):
        substring = string[i-4:i]
        good_string = True
        for char in substring:
            count = substring.count(char)
            if count > 1:
                good_string = False
        if good_string:
            print(i)
            break
