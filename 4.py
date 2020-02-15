#!/usr/bin/python
class PointColored(object):

    def __init__(self, red, green, blue, x, y):
        self.validation(red)
        self.validation(green)
        self.validation(blue)
        self.validation(x)
        self.validation(y)    
        self.x = x
        self.y = y
        self.red = red
        self.green = green
        self.blue = blue
        self.x = x
        self.y = y
        
    def validation(self, value):
        if value > 255 or value < 0:
            raise ValueError("Несоотвествущие значение числа. Оно должно лежать в диапозоне от 0 до 255.")
            
    def set_green(self, value):
        self.validation(value)
        self.green = value
            
    def set_blue(self, value):
        self.validation(value)
        self.blue = value
            
    def set_red(self, value):
        self.validation(value)
        self.red = value
    
    def set_x(self, value):
        self.validation(value)
        self.x = value
    
    def set_y(self, value):
        self.validation(value)
        self.y = value
        
    def get_green(self):
        return self.green
            
    def get_red(self):
        return self.red
            
    def get_blue(self):
        return self.blue
        
    def get_coordinate(self):
        return self.x, self.y
            
    def get_color(self):
        return self.red, self.green, self.blue
            
def banner():
    print("Что выхотите сделать с точкой?\n\t1. Узнать координаты.\n\t2. Установить новые координаты.\n\t3. Узнать значение цвета.\n\t4. Установить новые значения цвета.\nНапишите 0 для выхода.")


def color():
    print("Вы хотите изменить значение какой составляющей цвета?\n\t1. Красный.\n\t2. Зеленый.\n\t3. Синий.\n0. Выход.")
    
def coordinate():
    print("Вы хотете изменить координату.\n\t1. x\n\t2. y\n0. Отмена")
    
def validation(value, lst):
    if not(value in lst):
        print("Извините, мы не можем понять, что вы хотели.")
        
if __name__ == '__main__':
    r = input("r=")
    g = input("g=")
    b = input("b=")
    x = input("x=")
    y = input("y=")
    try:
        r = int(r)
        g = int(g)
        b = int(b)
    except ValueError:
        print('Значение цвета должно быть числом.')
        exit()
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print("Значение координат должно быть числом.")
        exit()
    p = PointColored(r, g, b, x, y)
    print("Вы создали точку.")
    value = ""
    while value != "0":
        v = ""
        banner()
        value = input("Введите номер ")
        main = ["0", "1","2", "3", "4"]
        colors = ["0", "1","2", "3",]
        coordinates = ["0", "1", "2"]
        validation(value, main)
        if value == "1":
            print("Координаты точки", p.get_coordinate())
        elif value == "2":
            while v != 0:
                coordinate()
                v = input("Введите номер ")
                validation(v, coordinates)
                if v == "1":
                    print("Текущая координата x=", p.get_coordinate()[0])
                    x = int(input("Введите число x="))
                    p.set_x(x)
                    print("Текущая координата x=", p.get_coordinate()[0])
                elif v == "2":
                    print("Текущая координата y=", p.get_coordinate()[1])
                    y = int(input("Введите число y="))
                    p.set_y(y)
                    print("Текущая координата y=", p.get_coordinate()[1])
                elif v != "0":
                     print("Введенное не поддается анализу.")
                else:
                    value = ""
                    break
        elif value == "3":
            print("Значение цвета точки", p.get_color)
        elif value == "4":
            while v != "0":
                color()
                value = input("Введите номер ")
                validation(value, colors)
                if value == "1":
                    print("Текущее значение красного", p.get_red())
                    r = int(input("Введите новое значение красного "))
                    p.set_red(r)
                    print("Текущее значение красного", p.get_red())
                elif value == "2":
                    print("Текущее значение зеленого", p.get_green())
                    r = int(input("Введите новое значение зеленого "))
                    p.set_green(r)
                    print("Текущее значение зеленого", p.get_green())
                elif value == "3":
                    print("Текущее значение синего", p.get_blue())
                    r = int(input("Введите новое значение синего "))
                    p.set_blue(r)
                    print("Текущее значение зеленого", p.get_blue())
                elif value == "0":
                    value = ""
                    break
                else:
                    print("Введенное не поддается анализу.")
