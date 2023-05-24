import random

# def algorytm_sieci_hopfilda():
#

def rand_x():
    x = random.randint(0, 1)
    return x

def matrix(xs, n):
    matrix_c=[[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:
                matrix_c[i][j]=0
            else:
                matrix_c[i][j]=(xs[i] - 0.5) * (xs[j] - 0.5)
    return matrix_c


# def x_t_plus_1(matrix, n):
#     for i in range(n):
#         if u[i] < 0:
#             x.append(0)
#         else if:
#
#         else:


def main():
    xs = [[0,0,0,0,0],
          [0,1,1,0,0],
          [0,0,1,0,0],
          [0,0,1,0,0],
          [0,0,1,0,0]]
    xs_s = [0,0,0,0,0,
          0,1,1,0,0,
          0,0,1,0,0,
          0,0,1,0,0,
          0,0,1,0,0]
    n = 25
    lista_x=[]
    for i in range(n):
        x = random.randint(0, 1)
        lista_x.append(x)
    print("x: ", lista_x)
    print("xs: ", xs)
    print("xs: ", xs_s)
    matrix_c = matrix(xs_s,n)
    print(matrix_c)
    #x_t_plus_1()
    w_i = matrix_c*2
    print("w_i", w_i)
    theta = [0 for i in range(n)]
    for i in range(n):
        theta[i]=sum(matrix_c[i])
    print("theta: ",theta)
    # t - liczba iteracji
    u = [0 for i in range(n)]
    for i in range(n):



if __name__ == "__main__":
    main()
