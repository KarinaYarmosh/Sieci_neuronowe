import math
import random


def fun(n,lista_x_old, lista_x_new,epsilon, c):
    lista_do_max = []
    for i in range(n):
        lista_do_max.append(lista_x_new[i] - lista_x_old[i])
    a = max(lista_do_max)
    while a > epsilon:
        x_old = lista_x_new[0]
        for i in range(n):
            xi_new = x_old - c*(df1(lista_x_old[0], lista_x_old[1], lista_x_old[2])/lista_x_old[i])
            print(xi_new)


def f1(x1,x2,x3):
    return 2*x1^2+2*x2^2+x3^2-2*x1*x2-2*x2*x3-2*x1+3

def df1(x1,x2,x3):
    return 4*x1+4*x2+2*x3-6

def main():
    c = 0.01
    epsilon =  0.00001
    N = 50
    #n = 2*N/c
    n=3
    lista_x_old=[]
    #for i in range(math.ceil(n)):
    #nie ma przedzilu!
    for i in range(n):
        xi_old = random.uniform(-N,N)
        print("xi_old: ", xi_old)
        lista_x_old.append(xi_old)
    lista_x_old.sort()
    print(lista_x_old)
    x_old_sum = sum(lista_x_old)
    print(x_old_sum)
    lista_x_new = []
    for i in range(n):
        xi_new = lista_x_old[i]-c*(df1(lista_x_old[0], lista_x_old[1], lista_x_old[2])/lista_x_old[i])
        print("x_new_", i, " :", xi_new)
        lista_x_new.append(xi_new)
    lista_x_new.sort()
    print(lista_x_new)
    fun(n,lista_x_old, lista_x_new,epsilon, c)

if __name__ == '__main__':
    main()
