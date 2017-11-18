

class OneLiner:
    def __init__(self, line):
        self.line = line

    def __repr__(self):
        return 'OneLiner("'+self.line+'")'

    def __str__(self):
        return '"'+self.line+'"'


class LinerList(list):
    def __init__(self, *lines):
        for line in lines:
            self.append(line)

    def __repr__(self):
        oneliners = ', '.join(map(repr, self))
        return 'LinerList('+oneliners+')'

    def __str__(self):
        lines = '\n'.join(map(str, self))
        return lines


CustomObject = OneLiner
CustomList = LinerList

#---------------------------------------------------------------

if __name__ == '__main__':
    mylist = LinerList(OneLiner('Hasta la vista, Baby'),
                        OneLiner("It's good to be bad"))
    print(mylist)
