import numpy as np
import random


def f(u, T=1):
    return 1 / (1 + np.exp(-(u / T)))


def matrix(n, xs, matrix_c):
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix_c[i][j] = 0
            else:
                matrix_c[i][j] = (xs[i] - 0.5) * (xs[j] - 0.5)

    return matrix_c


def boltzmann(n, theta, w, x, n_i, u, T, patterns, matches):
    for t in range(1, n_i):

        beta = [random.uniform(0, 1) for _ in range(n)]

        for i in range(n):
            u[i] = sum(w[i][j] * x[j] for j in range(n)) - theta[i]

        for i in range(n):
            x[i] = 1 if 0 <= beta[i] <= f(u[i], T=T) else 0

        for i in range(len(patterns)):
            if x == patterns[i]:
                matches[i] += 1

    return x, matches

def main():
    # Set the patterns
    patterns = [[0, 0, 0, 0, 0,
                 0, 1, 1, 0, 0,
                 0, 0, 1, 0, 0,
                 0, 0, 1, 0, 0,
                 0, 0, 1, 0, 0],
                [1, 1, 1, 1, 1,
                 1, 0, 0, 1, 1,
                 1, 1, 0, 1, 1,
                 1, 1, 0, 1, 1,
                 1, 1, 0, 1, 1]]

    matches = [0] * len(patterns)

    # Set the parameters
    T = 1
    n = 25
    num_iterations = 1000

    # Define the activation function

    # Initialize the Boltzmann machine variables
    z =[0, 0, 0, 0, 0,
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

    c = matrix(n,z,c)

    # Initialize weights
    w = np.array(2 * c, dtype=np.float64)

    # Initialize theta
    theta = np.zeros(n, dtype=np.float64)
    for i in range(n):
        theta[i] = sum(c[i])

    # Initialize u
    u = np.zeros(n, dtype=np.float64)


    x, matches=boltzmann(n,theta,w,x,num_iterations, u, T, patterns, matches)

    # Print the final state of the Boltzmann machine
    print("End:")
    print(str(np.array(x).reshape(5, 5)))

    # Print the number of matches
    print("Number of matches:")
    print(matches)

if __name__ == '__main__':
    main()
