import math

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

task_number = int(input("Введите номер задания "))
if task_number == 1:
    x = int(input("Введите координату x="))
    r = int(input("Введите радиус R="))
    if x >= -4 and x <= 6:
        print("Координата y=", task_1(x, r))
    else:
        print("Координата x лежит за пределами диапозона допустимых значений.")
elif task_number == 2:
    x = int(input("Введите координату x="))
    y = int(input("Введите координату y="))
    if task_2(x, y):
        print("Точка с координатами (", x, ",", y, ") попала в область.")
    else:
        print("Точка с координатами (", x, ",", y, ") не попала в область.")
