class Shelf:

    def __init__(self):
        self.contents = []

    
    def __getitem__(self, index):
        if len(self.contents) < index:
            return None
        else:
            return self.contents[index]

    def __setitem__(self, index, value):
        if len(self.contents) <= index:
            self.contents.append(value)
        else:
            self.contents[index] = value


