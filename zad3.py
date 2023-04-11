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
            lista_x_new[i] = lista_x_old[i] - c * dfx(lista_x_old[0], lista_x_old[1], lista_x_old[2])[i]
            print("X_NEW: ", lista_x_new[i])
            dla_f.append(lista_x_new[i])
        print("F: ", f(dla_f[0], dla_f[1], dla_f[2]))
        dla_f.clear()

def f(x1,x2,x3):
    return 2*x1**2 + 2*x2**2 + x3 - 2*x1*x2 - 2*x2*x3 - 2*x1 + 3

def dfx(x1,x2,x3):
    return [4*x1-2*x2-2, 4*x2-2*x3-2*x1, 2*x3-2*x2]

def main():
    c = 0.01
    epsilon = 0.0000001
    N = 50
    n = 3
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
        xi_new = lista_x_old[i] - c * dfx(lista_x_old[0], lista_x_old[1], lista_x_old[2])[i]
        lista_x_new.append(xi_new)
    print("LISTA X_NEW: ", lista_x_new)
    print("III")
    fun(n, lista_x_old, lista_x_new, epsilon, c)

if __name__ == '__main__':
    main()
