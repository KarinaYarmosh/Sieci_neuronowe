import math
import random


def fun(n, lista_x_old, lista_x_new, epsilon, c):
    while True:
        lista_max = []
        for i in range(n):
            a = abs(lista_x_new[i] - lista_x_old[i])
            lista_max.append(a)
        maxim = max(lista_max)
        print("MAX: ", maxim)
        if maxim <= epsilon:
            break
        dla_f = []
        for i in range(n):
            lista_x_old[i] = lista_x_new[i]
            lista_x_new[i] = lista_x_old[i] - c * dfx(lista_x_old[0], lista_x_old[1])[i]
            print("X_NEW: ", lista_x_new[i])
            dla_f.append(lista_x_new[i])
        print("F: ", f(dla_f[0], dla_f[1]))
        dla_f.clear()

def f(x1,x2):
    return 3*x1**4+4*x1**3-12*x1**2+12*x2**2-24*x2

def dfx(x1,x2):
    return [12*x1**3+12*x1**2-24*x1, 24*x2-24]

def main():
    c = 0.01
    epsilon = 0.0000001
    N = 5
    n = 2
    lista_x_old = []
    print("I")
    for i in range(n):
        xi_old = random.uniform(-N, N)
        lista_x_old.append(xi_old)
    lista_x_old.sort()
    print("LISTA X_OLD: ", lista_x_old)
    print("II")
    lista_x_new = []
    for i in range(n):
        xi_new = lista_x_old[i] - c * dfx(lista_x_old[0], lista_x_old[1])[i]
        lista_x_new.append(xi_new)
    print("LISTA X_NEW: ", lista_x_new)
    print("III")
    fun(n, lista_x_old, lista_x_new, epsilon, c)

if __name__ == '__main__':
    main()
