from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.geometry("400x400")
root.title('Plots')


def graph():
    plt.title('START', loc='right')

    # Красная прямая линия
    x = np.array([0, 6])
    y = np.array([0, 250])

    # Синяя линяя со звёздочками
    x1 = np.array([6, 8, 10, 16])
    y1 = np.array([0, 200, 0, 250])

    # Зелёная линия с точками
    y2 = np.array([250, 350, 150, 250])

    # Просто точки
    x_d = np.array([0, 6])
    y_d = np.array([200, 1])

    plt.plot(x, y, 'r', label='simple', marker='o', ms=20)
    plt.plot(x_d, y_d, 'o')
    plt.plot(x1, y1, 'o:b')
    plt.plot(y2, 'o--g')
    plt.grid()

    font = {
        'family': 'Times new roman',
        'color': 'magenta',
        'size': 15
    }

    plt.xlabel('x LABEL', fontdict=font)
    plt.ylabel('y LABEL', fontdict=font)

    plt.show()

btn = Button(root, text='Graph It!', command=graph).pack()


root.mainloop()