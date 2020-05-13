class QueueFIFO:

    def __init__(self):
        self.items:list = []


    def __len__(self):
        return len(self.items)

    def __getitem__(self, key):
        if key < len(self.items):
            return self.items[len(self.items)-key-1]
        else:
            raise IndexError('Index out of the range')

    def __str__(self):
        string: str = ''
        for i in range(len(self.items)-1, -1, -1):
            string += str(self.items[i])
            string += ' '
            if i % 10 == 0 and i != 0:
                string += '\n'
        return string


    def add_item(self, item):
        copy:list = []
        copy.append(item)
        for i in range(len(self.items)):
            copy.append(self.items[i])
        self.items = copy

    def del_item(self):
        copy:list = []
        for i in range(len(self.items)-1):
            copy.append(self.items[i])
        self.items = copy

    def search_item(self, item):
        key = 0
        while self.items[key] != item and key < len(self.items):
            key += 1
        if key == len(self.items) - 1:
            return -1
        else:
            return len(self.items) - key - 1



class StackLIFO:

    def __init__(self):
        self.items:list = []

    def __len__(self):
        return len(self.items)

    def __getitem__(self, key):
        return self.items[key]

    def __str__(self):
        string: str = ''
        for i in range(len(self.items)):
            string += str(self.items[i])
            string += ' '
            if i % 10 == 0 and i != 0:
                string += '\n'
        return string

    def add_item(self, item):
        copy: list = []
        copy.append(item)
        for i in range(len(self.items)):
            copy.append(self.items[i])
        self.items = copy

    def del_item(self):
        copy:list = []
        for i in range(1,len(self.items)):
            copy.append(self.items[i])
        self.items = copy

    def search_item(self, item):
        key = 0
        while key < len(self.items):
            if self.items[key] == item:
                return key
            else:
                key += 1
        key = -1
        return key

