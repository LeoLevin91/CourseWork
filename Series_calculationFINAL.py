import numpy as np
import matplotlib.pyplot as plt

eps = 0.00001


def fi(x, l):
    return 1 if 0.75 * l <= x <= 1.25 * l else 0


def f_n(n):
    if n == 0:
        return 0.25
    return (-2*np.sin(0.75*np.pi*n)) / (np.pi * n)


def v_x_t(n, c, k, l, x, t, s, alpha, u0):
    r = np.sqrt(s / np.pi)
    sum = 0
    for i in range(0, n):
        degree_exp = -(k*(np.pi**2)*(i**2) / ((l**2)*c) + 2*alpha/(r*c))
        sum = sum + (f_n(i) / (c*degree_exp) * (np.exp(degree_exp*t) - 1)) * np.cos(np.pi*i*x/l)
    return sum + u0


def show_plot(n, c, k, l, s, alpha, u0, t):
    print('Parameters:')
    print(f'n = {n}')
    print(f'c = {c}')
    print(f'k = {k}')
    print(f'l = {l}')
    print(f's = {s}')
    print(f'alpha = {alpha}')
    print(f'u0 = {u0}')
    print(f't = {t}')
    x = np.linspace(0, l, 1000)
    v = []
    for arg in x:
        v.append(v_x_t(n, c, k, l, arg, t, s, alpha, u0))
    fig, ax = plt.subplots()
    ax.set_title(f'Распределение температуры в стержне при t = {t}')
    ax.plot(x, v)
    ax.set_ylabel(f'V(x, {t})')
    ax.set_xlabel('Длина стержня')
    ax.grid()
    plt.show()


if __name__ == "__main__":
    show_plot(100, 1.65, 0.11, 8, 0.01, 0.003, 0, 30)