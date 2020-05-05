class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Linked_List:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'Linked_list [\n' + str(current.value) + '\n'
            while current.next is not None:
                current = current.next
                out += str(current.value) + '\n'
            return out + ']'
        return 'Linked_list []'


    def __getitem__(self, index):
        length = 0
        current = Node(None, None)
        if self.length != 0 and index < self.length:
            current = self.first
            while index != length:
                current = current.next
                length += 1
        return current.value

    def __len__(self):
        return self.length

    def insert(self, index, value):
        if self.first is None:
            self.first = Node(value, self.first)
            self.last = self.first.next
            return
        if index == 0:
            self.push(value)
            return
        current = self.first
        count = 0
        while current is not None:
            if count == index - 1:
                current.next = Node(value, current.next)
                if current.next is None:
                    self.last = current.next
                break
            current = current.next
            count += 1

    def clear(self):
        self.__init__()

    def add(self, x):
        self.length += 1
        if self.first is None:
            self.first = Node(x, None)
            self.last = self.first
        else:
            node = Node(x, None)
            self.last.next = node
            self.last = node

    def push(self, x):
        self.length += 1
        if self.first is None:
            self.first = Node(x, None)
            self.last = self.first
        else:
            self.first = Node(x, self.first)

    def pop(self):
        oldhead = self.first
        if oldhead is None:
            return None
        self.first = oldhead.next
        if self.first is None:
            self.last = None
        return oldhead.value

    def del_element(self, value):
        if self.length != 0:
            self.length -= 1
        if self.length != 0:
            self.length -= 1
        first = self.first
        if first is not None:
            if first.value == value:
                self.first = first.next
                first = None
                return
        while first is not None:
            if first.value == value:
                break
            last = first
            first = first.next
        if first is None:
            return
        last.next = first.next
        first = None

    def search(self, value):
        current = self.first
        count = 0
        while current is not None and current.value != value:
            if current.value == value:
                return count
            count += 1
            current = current.next
        return count