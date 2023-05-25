import numpy as np
import random

def matrix(matrix_c, n, xs):
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix_c[i][j] = 0
            else:
                matrix_c[i][j] = (xs[i] - 0.5) * (xs[j] - 0.5)
                
    return matrix_c


def hopfield(u, theta, num_iterations, n, w, x):
    for t in range(1, num_iterations):

        for i in range(n):
            u[i] = sum(w[i][j] * x[j] for j in range(n)) - theta[i]

        for i in range(n):
            if u[i] > 0:
                x[i] = 1
            elif u[i] < 0:
                x[i] = 0
                
    return x


def main():
    # Set the parameters
    n = 25
    num_iterations = 10

    # Initialize the Boltzmann machine variables
    xs =[0, 0, 0, 0, 0,
        0, 1, 1, 0, 0,
        0, 0, 1, 0, 0,
        0, 0, 1, 0, 0,
        0, 0, 1, 0, 0]

    # random x
    x=[]
    for i in range(n):
        a = random.randint(0, 1)
        x.append(a)
    print("x: ", x)

    # Initialize c
    c = np.zeros((n, n), dtype=np.float64)

    c = matrix(c,n,xs)

    # Initialize weights
    w = np.array(2 * c, dtype=np.float64)

    # Initialize theta
    theta = np.zeros(n, dtype=np.float64)
    for i in range(n):
        theta[i] = sum(c[i])

    # Initialize u
    u = np.zeros(n, dtype=np.float64)

    # Hopfield network algorithm
    x = hopfield(u, theta, num_iterations, n, w, x)

    # Print the final state of the Boltzmann machine
    print("End: ")
    print(str(np.array(x).reshape(5, 5)))

if __name__ == '__main__':
    main()
