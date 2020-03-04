import matplotlib.pyplot as plt

y_min = []
y_avg = []
y_max = []
x = []
for line in open("jump", "r"):
    n = 1
    while line[n] != ' ':
        n += 1
    try:
        y_min.append(float(line[1:n]))
    except ValueError:
        print()
    n = 32
    while line[n] != ' ':
        n += 1
    try:
        y_avg.append(float(line[32:n]))
    except ValueError:
        print()
    n = 63
    while line[n] != ' ':
        n += 1
    try:
       y_max.append(float(line[63:n]))
    except ValueError:
       print()
    n = 94
    while line[n] != ' ':
        n += 1
    try:
        x.append(int(line[94:n]))
    except ValueError:
       print()

plt.plot(x, y_min, 'g')
plt.ylabel('Время')
plt.xlabel('Длина массива')
plt.title('Поиск скачками')
plt.tight_layout()
plt.plot(x, y_avg, 'b')
plt.plot(x, y_max, 'r')
plt.grid()
plt.savefig('jump')
