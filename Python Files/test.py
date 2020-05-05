import matplotlib.pyplot as plt

x = []
for i in range(-100,100):
    x.append(i)
y = []
y1 = []
for i in range(-100,100):
    y.append(i ** 2)
for i in range(-100,100):
    y1.append(i)
plt.figure(figsize=(len(x)/10, len(y)/10))
plt.plot(x, y, y1)               # построение графика
plt.title("y = x^2") # заголовок
plt.ylabel("y", fontsize=14) # ось ординат
plt.xlabel("x", fontsize=14)
plt.grid(True)# включение отображение сетки
plt.savefig("y=x^2")