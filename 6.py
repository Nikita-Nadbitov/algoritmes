import random
import operator

def initizialtion(arr, n):
    for i in range(n):
        arr.append(random.randint(0,100))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                #swap values
                arr[j], arr[j+1] = arr[j+1], arr[j]

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

def coctail_sort(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        for i in range(left, right, +1):
            if arr[i] > arr[i + 1]:
                # swap values
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right -= 1

        for i in range(right, left, -1):
            if arr[i - 1] > arr[i]:
                # swap values
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
        left += 1


def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i > -1 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i + 1] = key


def merge_sort(a):
    n = len(a)
    if n < 2:
        return a

    l = merge_sort(a[:n//2])
    r = merge_sort(a[n//2:n])

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


vector = []
initizialtion(vector, 10)
print(vector)
vector = merge_sort(vector)
print(vector)