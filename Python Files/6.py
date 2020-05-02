import random
import time
import matplotlib.pyplot as plt


def initizialtion(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0,100))
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def gnome_sort(arr):
    i = 0
    while i < len(arr)-1:
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            if i == 0:
                i += 1
            else:
                i -= 1
        elif i == 0:
            i += 1
        else:
            i += 1
    return arr


def coctail_sort(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        for i in range(left, right, +1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right -= 1

        for i in range(right, left, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
        left += 1
    return arr


def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i > -1 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr


def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return arr
    l = merge_sort(arr[:n // 2])
    r = merge_sort(arr[n // 2:n])
    i = j = 0
    res = []
    while i < len(l) or j < len(r):
        if not i < len(l):
            res.append(r[j])
            j += 1
        elif not j < len(r):
            res.append(l[i])
            i += 1
        elif l[i] < r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
    return res


def minimum(arr, start_position, end_position):
    minimum_index = -1
    for i in range(start_position, end_position):
        if arr[i] < arr[minimum_index]:
            minimum_index = i
    return minimum_index


def selection_sort(arr):
    for i in range(len(arr)):
        min_indx = minimum(arr, i, len(arr))
        if min_indx != i:
            arr[i], arr[min_indx] = arr[min_indx], arr[i]
    return arr


def combsort(arr):
    n = len(arr)
    width = (n * 10 // 13) if n > 1 else 0
    while width:
        if 8 < width < 11:
            width = 11
        swapped = False
        for i in range(n - width):
            if arr[i + width] < arr[i]:
                arr[i], arr[i + width] = arr[i + width], arr[i]
                swapped = True
        width = (width * 10 // 13) or swapped
    return arr

def quicksort(arr):
   if len(arr) <= 1:
       return arr
   else:
       q = random.choice(arr)
       s_nums = []
       m_nums = []
       e_nums = []
       for n in arr:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quicksort(s_nums) + e_nums + quicksort(m_nums)


def runtime(n, key_dict=0):
    max_time = 0
    arr = initizialtion(n)
    dict = {0: bubble_sort, 1:gnome_sort, 2:coctail_sort, 3:insertion_sort, 4:merge_sort, 5:selection_sort, 6:combsort, 7:quicksort}
    s = 0
    for i in range(50):
        start_time = time.monotonic()
        arr = dict[key_dict](arr)
        run = time.monotonic() - start_time
        if i == 0:
            min_time = run
            max_time = run
        else:
            min_time = min(run, min_time)
            max_time = max(run, max_time)
        s += run
    return min_time, s/50, max_time

n = 10
n_count = []
avg = []
mini = []
maximum = []
while n < 1000000:
    result = runtime(n, 0)
    n_count.append(n)
    avg.append(result[1])
    maximum.append(result[2])
    mini.append(result[0])
    print(n)
    if n < 100:
        n += 10
    elif n < 1000:
        n += 100
    elif n < 10000:
        n += 1000
    elif n < 100000:
        n += 10000
    else:
        n += 100000

plt.plot(n_count, avg, 'g')
plt.ylabel('Время')
plt.xlabel('Длина массива')
plt.title('Сортировка пузырьком')
plt.tight_layout()
plt.plot(n_count, mini, 'b')
plt.plot(n_count, maximum, 'r')
plt.grid()
plt.savefig('bubble')