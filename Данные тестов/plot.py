import numpy as np
import matplotlib.pyplot as plt


def func(x):
    return np.sqrt((10 ** 10) / ((10 ** 4 - 4 * np.pi ** 2 * x ** 2) + 4 * np.pi ** 2 * x ** 2))

if __main__ == '__main__':
    x = np.linspace(10 ** 8, 10 ** 12, 10 ** 9, dtype=np.float64)
    y = np.float64(func(x))
    print(len(x))

    plt.loglog(x, y, 'g')
    plt.ylabel('Время')
    plt.xlabel('Длина массива')
    plt.title("Интерполяционный поиск")
    plt.tight_layout()
    plt.grid()
    plt.show()
    plt.savefig()