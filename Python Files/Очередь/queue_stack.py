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

def add_value(data_structure, value):
    data_structure.add_item(value)

def split_text(text:str, number:int):
    ctext = text.split(' ')
    msg = ''
    msg_ret = []
    i = 0
    while i <= len(ctext) - 1:
        if i == 0 or msg == '':
            msg += ctext[i]
            i += 1
        elif len(msg) + len(ctext[i]) + 1 <= number and msg != '':
            msg += ' '
            msg += ctext[i]
            i += 1
        else:
            msg_ret.append(msg)
            msg = ''
    msg_ret.append(msg)
    return msg_ret


print(split_text('доброе утро', 3))
print(split_text('у нас хорошая погода', 5))
print(split_text('погода хорошая у всех нас', 15))