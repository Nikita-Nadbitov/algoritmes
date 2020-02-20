import math
import random

def task_1(x, r):
    if x >= -4 and x <= 0:
        return -0.5 * x
    elif x > 0 and x <= 2:
        return -(math.sqrt(r ** 2 - (x - 0) ** 2) - 2)
    elif x > 2 and x <= 4:
        return (math.sqrt(r ** 2 - (x - 2) ** 2) - 0)
    elif x > 4 and x <= 5:
        return -x + 4
        
def task_2(x, y):
    if (y < x and y > ((x - 2) ** 2 - 3) and y > 0):
        return(True)
    elif (y < 0 and x > y and y > ((x - 2) ** 2 -3)):
        return(True)
    else:
        return(False)
        
def line_for_table():
    print('{:<1} {:<10} {:<1} {:<10} {:<1}'.format("+","-"*10, "+", "-"*10, '+'))
        
def header_table():
    line_for_table()
    print('{:<1} {:<10} {:<1} {:<10} {:<1}'.format('|', 'x', "|",'y','|'))
    line_for_table()
    
def table(dx, r):
    x0 = -4.0
    x1 = 6.0
    header_table()
    while x0 != x1:
        z = round(x0, 8)
        y = task_1(x0, r)
        print('{:<1} {:<10} {:<1} {:<10} {:<1}'.format('|', z, '|', y, '|'))
        line_for_table()
        x0 += dx

def series(x0, x, y0, y):
    i = 1
    while i <= 10:
        x1 = round(random.uniform(x0, x), 3)
        y1 = round(random.uniform(y0, y), 3)
        if task_1(x1, y1):
            print("Выстрел ", i, "-ый с координатами x=", x1, ", y=", y1, " попал в мишень.")
        else:
            print("Выстрел ", i, "-ый с координатами x=", x1, ", y=", y1, "не попал в мишень.")
        i += 1

def teilor(x, n):
    n0 = 1
    sum = 0
    while n0 <= n:
        n1 = 1
        proizved_znam = 1
        proizved_chis = 1
        while n1 <= n0:
             proizved_znam *= 2 * n1 + 1
             if n1 != n0:
                proizved_chis *= 2 * n1
             else:
                proizved_chis = proizved_chis * (2 * n1 - 1)
             n1 = n1 + 1
        
        proizved_chis *= x ** (2 * n + 1)
        sum += proizved_chis/proizved_znam
        n0 = n0 + 1
    sum = math.pi/2 - (x + sum)
    return round(sum, n)

def table_tailor(x, x0, dx, n):
    header_table()
    while x0 < x:
        line_for_table()
        print('{:<1} {:<10} {:<1} {:<10} {:<1}'.format('|', round(x0, 8), "|", round(teilor(x0, n), 8), '|'))
        line_for_table()
        x0 += dx
    
task_number = int(input("Введите номер задания "))
if task_number == 1:
    dx = float(input("Введите шаг dx="))
    r = float(input("Введите радиус r="))
    table(dx, r)
elif task_number == 2:
    x0 = float(input("Введите начало диапозона координат x, x0="))
    x = float(input("Введите окончание диапозона координат x, x="))
    y0 = float(input("Введите начало диапозона координат x, y0="))
    y = float(input("Введите окончание диапозона координат y, y="))
    series(x0, x, y0, y)
elif task_number == 3:
    x0 = float(input("Введите x из диапозона от -1 до 1, x0="))
    x = float(input("Введите x из диапозона от -1 до 1, x > x0, x="))
    dx = float(input("Введите шаг приращения, dx="))
    n = int(input("Введите число шагов для ряда Тейлора, n="))
    table_tailor(x, x0, dx, n)
else:
    print("Неправильный номер.")
