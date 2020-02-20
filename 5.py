import random
import timeit
import matplotlib.pyplot as plt

def linear_search(array, key):
    for i in range(len(array)):
        if array[i] == key:
            return i
    return -1


# длина массива arr
key = 956525#что ищем
time = []#среднее время поиска
len_arr = []#длина массива поиска
min_arr = []#минимальное время поиска
max_arr = []#максимальное время поиска
for i in range(1000000):
  minimum = 15#
  maximum = 0#
  summ = 0
  arr = []#где ищем
  if i % 100000 == 0:
    for k in range(50):
      for j in range(i):
          arr.append(random.randint(-100000000, 100000000))
      start = timeit.default_timer()
      linear_search(arr, key)
      timer = timeit.default_timer()-start
      summ += timer
      if minimum > timer:
        minimum = timer
      elif maximum < timer:
        maximum = timer
      arr = []
    len_arr.append(i)
    time.append(summ/50)
    min_arr.append(minimum)
    max_arr.append(maximum)
    del minimum, maximum, summ
    print(i)
plt.figure(figsize=(len(len_arr)*5, len(time)*5))
plt.plot(len_arr, time)               # построение графика
plt.title("time ot len arr") # заголовок
plt.ylabel("time", fontsize=14) # ось ординат
plt.xlabel("length of array", fontsize=14)
plt.grid(True)# включение отображение сетки
plt.savefig("linear_search_google_collab.png")
file = open("Результаты для linear_search_google_collab", "w")
file.write('{:<1}{:<30}{:<1}{:<30}{:<1}{:<30}{:<1}{:<30}{:<1}'.format("+", "-"*30, "+", "-"*30,"+", "-"*30,"+","-"*30,"+")+ '\n')
file.write('{:<1}{:<30}{:<1}{:<30}{:<1}{:<30}{:<1}{:<30}{:<1}'.format("|", "Минимальное время", "|", "Среднее время по 50 итерациям","|", "Максимальное время","|","Длина массива","|") + '\n')
file.write('{:<1}{:<30}{:<1}{:<30}{:<1}{:<30}{:<1}{:<30}{:<1}'.format("+", "-"*30, "+", "-"*30,"+", "-"*30,"+","-"*30,"+\n")+ '\n')
for i in range(len(min_arr)):
  file.write('{:<1}{:<30}{:<1}{:<30}{:<1}{:<30}{:<1}{:<30}{:<1}'.format("|", min_arr[i], "|", time[i],"|", max_arr[i],"|",len_arr[i],"|")+ '\n')
  file.write('{:<1}{:<30}{:<1}{:<30}{:<1}{:<30}{:<1}{:<30}{:<1}'.format("+", "-"*30, "+", "-"*30,"+", "-"*30,"+","-"*30,"+")+ '\n')
file.close()