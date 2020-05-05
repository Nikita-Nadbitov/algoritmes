import math

m = int(input("Введите значение m = "))
n = int(input("Введите значение n = "))
try:
    z1 = ((m - 1) * math.sqrt(m) - (n - 1) * math.sqrt(n)) / (math.sqrt(m ** 3  * n) + n*m + m ** 2 - m)
except ZeroDivisionError:
    print("Извините, текущие значения m=", m, "и n=", n, "не подходят")
    z1 = None
try:
    z2 = (math.sqrt(m) - math.sqrt(n)) / (m)
except ZeroDivisionError:
    print("Извините, текущие значения m=", m, "и n=", n, "не подходят")
    z2 = None
print ("z1 =", z1, "z2 =", z2)
