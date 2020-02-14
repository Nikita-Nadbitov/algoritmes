import math

m = int(input("Введите значение m = "))
n = int(input("Введите значение n = "))
z1 = ((m - 1) * math.sqrt(m) - (n - 1) * math.sqrt(n)) / (math.sqrt(m ** 3  * n) + n*m + m ** 2 - m)
z2 = (math.sqrt(m) - math.sqrt(n)) / (m)
print ("z1 = ", z1, "z2 = ", z2)
