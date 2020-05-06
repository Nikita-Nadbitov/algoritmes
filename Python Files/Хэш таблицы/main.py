from dataclasses import dataclass
from typing import List


@dataclass
class TInfo:
    phone: str = ''
    family: str = ''
    name: str = ''


@dataclass
class HashItem:
    info: TInfo
    empty: bool = True
    visit: bool = False


class Hash:
    info: TInfo

    def __init__(self, table_size=10):
        self.table_size = table_size
        self.info = TInfo()
        self.hash_table = [HashItem(info=self.info) for _ in range(self.table_size)]
        self.size = 0
        self.step = 21

    def __hash_function(self, value):
        result = 0
        for i in value:
            result += ord(i)
            result %= self.table_size
        return result

    def add_hash(self, name: str, family: str, phone: str) -> int:
        adr = -1
        if self.size < self.table_size:
            adr = self.__hash_function(phone)
            while not self.hash_table[adr].empty:
                adr = (adr + self.step) % self.table_size
            self.hash_table[adr].empty = False
            self.hash_table[adr].visit = True
            contact = TInfo(name=name, family=family, phone=phone)
            self.hash_table[adr].info = contact
            self.size += 1
        return adr

    def __clear_visit(self):
        for i in self.hash_table:
            i.visit = False

    def find_hash(self, phone):
        result = -1
        ok: bool
        fio = ""
        count = 1
        self.__clear_visit()
        i = self.__hash_function(phone)
        ok = self.hash_table[i].info.phone == phone
        while not ok and not self.hash_table[i].visit:
            count += 1
            self.hash_table[i].visit = True
            i = (i + self.step) % self.table_size
            ok = self.hash_table[i].info.phone == phone
        if ok:
            result = i
            fio = self.hash_table[result].info
        return result, fio

    def del_hash(self, phone):
        result = False
        i = 0
        if self.size != 0:
            i = self.__hash_function(phone)
            if self.hash_table[i].info.phone == phone:
                self.hash_table[i].empty = True
                result = True
                self.size -= 1
            else:
                i = self.find_hash(phone)
                if i == -1:
                    self.hash_table[i].empty = True
                    result = True
                    self.size -= 1
        return result

    def print(self):
        print("{:<6}{:<20}{:<20}{:<20}".format("N", "NAME", "FAMILY", "PHONE"))
        for i in range(self.table_size):
            name: str = self.hash_table[i].info.name
            family = self.hash_table[i].info.family
            phone = self.hash_table[i].info.phone
            print("{:<6}{:<20}{:<20}{:<20}".format(i + 1, name, family, phone))
        print()