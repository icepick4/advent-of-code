def read_file(filename):
    string = ''
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            string += line
    return string


if __name__ == '__main__':
    string = read_file('input.txt')
    # change to 4 the value 14 for the first part
    for i in range(14, len(string)):
        substring = string[i-14:i]
        good_string = True
        for char in substring:
            count = substring.count(char)
            if count > 1:
                good_string = False
        if good_string:
            print(substring)
            print(i)
