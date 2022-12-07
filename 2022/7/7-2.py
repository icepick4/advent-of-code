def read_file(filename):
    actions = []
    contents = []
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('$'):
                actions.append(line.strip())
            elif last_line and last_line.startswith('$'):
                contents.append('new')
                contents.append(line.strip())
            else:
                contents.append(line.strip())
            last_line = line
    return actions, contents


class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        self.files = []

    def add_child(self, child):
        self.children.append(child)

    def add_file(self, file):
        self.files.append(file)

    def already_child(self, name):
        for child in self.children:
            if child.name == name:
                return True
        return False

    def already_file(self, name):
        for file in self.files:
            if file.name == name:
                return True
        return False

    def calculate_size(self):
        size = 0
        for file in self.files:
            size += file.size
        for child in self.children:
            size += child.calculate_size()
        return size

    def browse(self):
        for child in self.children:
            if 3000000 > child.calculate_size() > 2677139:
                print(child.calculate_size())
            child.browse()


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


if __name__ == '__main__':
    actions, contents = read_file('input.txt')
    directory = Directory('/')
    actions = actions[1:]
    contents = contents[1:]
    for action in actions:
        print(action)
        if action.startswith('$ cd ..'):
            print('je remonte au dossier', directory.parent.name)
            directory = directory.parent
        elif action.startswith('$ cd'):
            print('je descends au dossier', action.split(' ')[-1])
            if directory.already_child(action.split(' ')[-1]):
                for child in directory.children:
                    if child.name == action.split(' ')[-1]:
                        directory = child
                        break
            else:
                directory.add_child(
                    Directory(action.split(' ')[-1], directory))
                directory = directory.children[-1]
        elif action.startswith('$ ls'):
            print('je liste le dossier', directory.name)
            for i, content in enumerate(contents):
                if content.startswith('dir'):
                    print('j\'ajoute le dossier', content.split(
                        ' ')[-1], 'au dossier', directory.name)
                    directory.add_child(
                        Directory(content.split(' ')[-1], directory))
                elif content.startswith('new'):
                    break
                else:
                    print('j\'ajoute le fichier', content.split(
                        ' ')[0], 'au dossier', directory.name)
                    directory.add_file(
                        File(content.split(' ')[1], int(content.split(' ')[0])))
            contents = contents[i + 1:]
    while directory.parent:
        directory = directory.parent
    print(directory.calculate_size())
    directory.browse()
