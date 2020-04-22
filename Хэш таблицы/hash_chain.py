from dataclasses import dataclass


@dataclass
class TInfo:
    name: str = ''
    family: str = ''
    phone: str = ''


@dataclass
class SubCell:
    info: TInfo = TInfo(name='', family='', phone='')


class ChainHashTable:

    def __init__(self, table_size = 100):
        self.table_size = table_size
        self.info = TInfo()
        self.hash_table = [[SubCell(self.info)] for _ in range(self.table_size)]
        self.step = 1

    def __hash_func(self, value):
        result = 0
        for i in value:
            result += ord(i)
            result %= self.table_size
        return result

    def add_item(self, info:TInfo):
        adr = self.__hash_func(info.phone)
        i = len(self.hash_table[adr]) - 1
        self.hash_table[adr][i] = SubCell(info=info)
        self.hash_table[adr].append(SubCell(info=TInfo()))

    def del_item(self, info):
        adr = self.__hash_func(info.phone)
        i = 0
        while self.hash_table[adr][i].info != info:
            i+=1
        del self.hash_table[adr][i]

    def print(self):
        print("{:<6}{:<1}{:<6}{:<20}{:<20}{:<20}".format("N", "/", "N", "NAME", "FAMILY", "PHONE"))
        for i in range(self.table_size):
            for j in range(len(self.hash_table[i])):
                name: str = self.hash_table[i][j].info.name
                family = self.hash_table[i][j].info.family
                phone = self.hash_table[i][j].info.phone
                print("{:<6}{:<1}{:<6}{:<20}{:<20}{:<20}".format(i + 1, '.', j+1, name, family, phone))
        print()
