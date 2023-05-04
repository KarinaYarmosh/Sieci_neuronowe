import math
import random


def x_p(u, w, beta):
    xp = list()
    # dla każdego z 4 zbiorów x-ów
    for p in range(4):
        x_p_i = []
        for i in range(2):
            suma = 0
            for j in range(3):
                suma = suma + w[i][j] * u[p][j]
            suma = f(suma, beta)
            x_p_i.append(suma)
        x_p_i.append(1)
        xp.append(x_p_i)
    return xp

def y_p(x, s, beta):
    yp = list()
    for p in range(4):
        suma = 0
        for i in range(3):
            suma = suma + x[p][i] * s[i]

        suma = f(suma, beta)
        yp.append(suma)
    return yp


def dE_dS(y, z, s, x, i, beta, p):
    suma_wew = 0.0
    for k in range(3):
        suma_wew = suma_wew + (s[k] * x[p][k])

    suma_1 = (y[p] - z[p]) * df_dx(suma_wew, beta) * x[p][i]
    return suma_1


def dE_Dwij(y, z, s, x, w, u, i, j, beta, p):
    suma_wew1 = 0.0
    for k in range(3):
        suma_wew1 = suma_wew1 + s[k] * x[p][k]
    suma_wew1 = df_dx(suma_wew1, beta)

    suma_wew2 = 0.0
    for l in range(3):
        suma_wew2 = suma_wew2 + w[i][l] * u[p][l]
    suma_wew2 = df_dx(suma_wew2, beta)

    suma = (y[p] - z[p]) * suma_wew1 * s[i] * suma_wew2 * u[p][j]

    return suma


def f(x, beta):
    return (1 / (1 + math.exp((-1) * beta * x)))


def df_dx(x, beta):
    return beta*math.exp(-beta*x) / (1+math.exp(-beta*x))**2

def main_func(u, z, beta, c, epsilon, w_old, s_old,p):
    xp = x_p(u, w_old, beta)
    yp = y_p(xp, s_old, beta)
    s_new = []
    w_new = []
    for i in range(3):
        s_new.append(s_old[i] - c * dE_dS(yp, z, s_old, xp, i, beta,p))

    for i in range(2):
        w = []
        for j in range(3):
            w.append(w_old[i][j] - c * dE_Dwij(yp, z, s_old, xp, w_old, u, i, j, beta,p))
        w_new.append(w)

    return w_new, s_new

def xor_bp(u, z, beta, c, epsilon, w_old, s_old):
    p = random.randint(0, 3)
    w_new, s_new = main_func(u, z, beta, c, epsilon, w_old, s_old, p)
    while True:
        max_w = 0
        p = random.randint(0, 3)
        w_roznicy = []
        for i in range(2):
            for j in range(3):
                w_roznicy.append(abs(w_old[i][j] - w_new[i][j]))
        max_w = max(w_roznicy)

        max_s = 0
        s_roznicy = []
        for i in range(3):
            s_roznicy.append(abs(s_old[i] - s_new[i]))
        max_s = max(s_roznicy)

        max_wszystkow = max(max_s, max_w)

        if max_wszystkow < epsilon:
            print("KONIEC")
            print(y_p(x_p(u, w_new, beta), s_new, beta))
            print(w_old)
            print(s_old)
            break

        s_old = s_new
        w_old = w_new

        w_new, s_new = main_func(u, z, beta, c, epsilon, w_old, s_old, p)

def main():
    c = 1
    epsilon = 0.00001
    beta = 1

    w_old = [[0, 1, 2], [0, 1, 2]]
    s_old = [0, 1, 2]

    u = [[0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1]]
    z = [0, 1, 1, 0]
    xor_bp(u, z, beta, c, epsilon, w_old, s_old)


if __name__ == "__main__":
    main()
