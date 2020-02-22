import math
import random
import time
#import matplotlib.pyplot as plt


def linear_search(array, key):
    for i in range(len(array)):
        if array[i] == key:
            return i
    return -1


def binar_search(array, key):
    minimum = 0
    maximum = len(array) - 1
    ret = 0
    while minimum <= maximum:
        mid = (maximum + minimum) // 2
        if key < array[mid]:
            maximum = mid - 1
        elif key > array[mid]:
            minimum = mid + 1
        else:
            ret = mid
            break
    while ret > 0 and array[ret - 1] == key:
        ret -= 1
    if array[ret] == key:
        return ret
    else:
        return -1


def interpolation_search(array, key):
    minimum = 0
    maximum = len(array) - 1
    ret = 0
    while array[minimum] < key < array[maximum]:
        mid = int(minimum + (maximum - minimum) * (key - array[minimum]) / (array[maximum] - array[minimum]))
        if array[mid] == key:
            ret = mid
            break
        elif array[mid] > key:
            maximum = mid - 1
        else:
            minimum = mid + 1

    if array[minimum] == key:
        ret = minimum
    if array[maximum] == key:
        ret = maximum
    while ret > 0 and array[ret - 1] == key:
        ret -= 1
    if array[ret] == key:
        return ret
    else:
        return -1


def jump_search(array, key):
    length = len(array)
    jump_step = int(math.sqrt(length))
    previous: int = 0
    while array[min(jump_step, length) - 1] < key:
        previous = jump_step
        jump_step += int(math.sqrt(length))
        if previous >= length:
            return -1
    while array[previous] < key:
        previous += 1
        if previous == min(jump_step, length):
            return -1
    if array[previous] == key:
        return previous
    return -1

def generation(n, first, last):
    array = []
    for i in range(n):
        array.append(random.randint(first, last))
    return array


def choose_algorithm_for_search(array, key, type='linear_search'):
    if type == 'linear_search':
        starttime = time.monotonic()
        linear_search(array, key)
        runtime = time.monotonic() - starttime
    elif type == 'binar_search':
        starttime = time.monotonic()
        binar_search(array, key)
        runtime = time.monotonic() - starttime
    elif type == 'interpolation_search':
        starttime = time.monotonic()
        interpolation_search(array, key)
        runtime = time.monotonic() - starttime
    elif type == 'jump_search':
        starttime = time.monotonic()
        jump_search(array, key)
        runtime = time.monotonic() - starttime
    else:
        raise ValueError("Неизвестное значение type", type)
        exit()
    return runtime

def time_for_algorithms_search(array, key, type='linear_search'):
    sum = 0
    for i in range(50):
        if i != 0:
            array.sort()
            array = generation(len(array), array[0], array[len(array)-1])
        runtime = choose_algorithm_for_search(array, key, type)
        if i == 0:
            minimum = runtime
            maximum = runtime
        elif minimum > runtime:
            minimum = runtime
        elif maximum < runtime:
            maximum = runtime
        sum = + runtime
    return minimum, sum / 50, maximum


def get_time(*args, key, reqired_vector):
    list_type_search = ['binar_search', 'linear_search', 'jump_search', 'interpolation_search']
    for i in range(len(args)):
        args[i].append(time_for_algorithms_search(reqired_vector, key, list_type_search[i]))


def print_to_file(args, length, filename):
    file = open(filename, "w")
    file.write('{:<1}{:<30}{:<1}{:<30}{:<1}{:<30}{:<1}{:<30}{:<1}'.format("|", "Минимальное время", "|",
                                                                          "Среднее время по 50 итерациям", "|",
                                                                          "Максимальное время", "|",
                                                                          "Длина массива", "|") + '\n')
    for j in range(len(args)):
        file.write('{:<1}{:<30}{:<1}{:<30}{:<1}{:<30}{:<1}{:<30}{:<1}'.format("|", args[j][0], "|", args[j][1], "|", args[j][2], "|", length[j], "|") + '\n')
    file.close()


n = 10000000
s = 121

vector = generation(n, -1000, 1000)
run_bin = []
run_lin = []
run_inter = []
run_jump = []
length_ar = []

while 1000 >= n:
        get_time(run_bin, run_lin, run_jump, run_inter, key=s, reqired_vector=vector)
        length_ar.append(n)
        n += 10000000
print_to_file(run_bin, length_ar, 'binar_10000000_100000000')
print_to_file(run_lin, length_ar, 'linar_10000000_100000000')
print_to_file(run_jump, length_ar, 'jump_search_10000000_100000000')
print_to_file(run_inter, length_ar, 'inter_10000000_100000000')