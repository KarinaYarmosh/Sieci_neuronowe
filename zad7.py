import numpy as np


def f(x, beta=2.5):
    return 1 / (1 + np.exp(-beta * x))


def dfdx(x, beta):
    return f(x, beta) * (1 - f(x, beta))


def mse(y, target):
    return np.mean((target - y)**2) / len(y)

def main():
    print("Zadanie 1")

    # define input data
    u1 = np.array([1, 1, 0,
                   0, 1, 0,
                   0, 1, 0,
                   1])  # 1 - bias

    u2 = np.array([0, 0, 1,
                   0, 0, 1,
                   0, 0, 1,
                   1])  # 1 - bias

    u = np.array([u1, u2]).reshape(2, 10)

    # define weights
    w = np.array([[20.0, 0.0, 0.0,
                   0.0, 0.0, 0.0, 0.0,
                   0.0, 0.0, -10.0],
                  [0.0, 0.0, 20.0,
                   0.0, 0.0, 0.0, 0.0,
                   0.0, 0.0, -10.0]])

    # column with -10 for s
    s3 = np.full_like(u1, -10)

    # s is a matrix with u1, u2 and -10 as a columns
    s = np.column_stack((20 * u1, 20 * u2, s3))

    x = np.column_stack((u.dot(w.T), np.ones(2)))
    print("x dla u1: " + str(x[0]))
    print("x dla u2: " + str(x[1]))
    print()

    y = f(s.dot(x.T).T)
    print("y dla u1: \n" + str(np.round(y[0][:-1].reshape(3, 3), 2)) + "\n")
    print("y dla u2: \n" + str(np.round(y[1][:-1].reshape(3, 3), 2)) + "\n")

    print("Zadanie 2")

    c = 0.8
    eps = 0.0001
    beta = 1.0
    learning_rate = 0.1
    w_new = w.copy()
    s_new = s.copy()
    u_copy = u.copy()

    error = np.inf
    epoch = 1
    while error > eps:

        # Forward pass
        x = np.column_stack((u.dot(w_new.T), np.ones(2)))
        y = f(s_new.dot(x.T).T)

        # Calculate the error
        error = mse(y[:, :-1].reshape(2, 9), u[:, :-1].reshape(2, 9))
        #print(f"Epoch: {epoch}, Error: {error}")

        # transpose u and y for easier calculations using matrix multiplication
        u_copy = u_copy.T
        y = y.T

        dEds = np.zeros_like(s_new)
        for j in range(len(dEds)):
            for i in range(len(dEds[j])):
                # dEds[j, i] = (y[j] - u_copy[j]) * dfdx(s_new[j].dot(x.T) * x.T[i])
                for p in range(len(u)):
                    dEds[j, i] += (y[j, p] - u_copy[j, p]) * \
                                  dfdx(s_new[j].dot(x[p].T), beta) * x[p, i]

        dEdw = np.zeros_like(w_new)
        for i in range(len(dEdw)):
            for j in range(len(dEdw[i])):
                for p in range(len(u)):
                    for t in range(len(u[p])):
                        dEdw[i, j] += (y[t, p] - u_copy[t, p]) * dfdx(s_new[t].dot(x[p]), beta) * \
                                      dfdx(w_new[i].dot(u[p].T), beta) * \
                                      u[p, j]

        # Update weights
        s_new = s_new - learning_rate * dEds
        w_new = w_new - learning_rate * dEdw

    # Forward pass
    x = np.column_stack((u.dot(w_new.T), np.ones(2)))
    y = f(s_new.dot(x.T).T)

    # print results
    print("y dla u1: \n" + str(np.round(y[0][:-1].reshape(3, 3), 2)))
    print()
    print("y dla u2: \n" + str(np.round(y[1][:-1].reshape(3, 3), 2)))

    print("w po backpropagation:")
    print(w_new)
    print()

    print("s po backpropagation:")
    print(s_new)

    print("Zadanie 3")

    # init parameters and weights
    N = 1
    w_new = np.random.uniform(-N, N, (2, 10))
    #print(w_new)
    s_new = np.random.uniform(-N, N, (10, 3))
    #print(s_new)
    u_copy = u.T.copy()

    error = np.inf
    epoch = 1
    while error > eps:

        # Forward pass
        x = np.column_stack((u.dot(w_new.T), np.ones(2)))
        y = f(s_new.dot(x.T).T)

        # Calculate the error
        error = mse(y[:, :-1].reshape(2, 9), u[:, :-1].reshape(2, 9))
        #print(f"Epoch: {epoch}, Error: {error}")

        # transpose u and y for easier calculations using matrix multiplication
        y = y.T

        dEds = np.zeros_like(s_new)
        for j in range(len(dEds)):
            for i in range(len(dEds[j])):
                for p in range(len(u)):
                    dEds[j, i] += (y[j, p] - u_copy[j, p]) \
                                  * dfdx(s_new[j].dot(x[p].T), beta) * x[p, i]

        dEdw = np.zeros_like(w_new)
        for i in range(len(dEdw)):
            for j in range(len(dEdw[i])):
                for p in range(len(u)):
                    for t in range(len(u[p])):
                        dEdw[i, j] += (y[t, p] - u_copy[t, p]) * dfdx(s_new[t].dot(x[p]), beta) \
                                      * dfdx(w_new[i].dot(u[p].T), beta) * \
                                      u[p, j]

        # Update weights
        s_new = s_new - learning_rate * dEds
        w_new = w_new - learning_rate * dEdw
        epoch += 1

    # Forward pass
    x = np.column_stack((u.dot(w_new.T), np.ones(2)))
    y = f(s_new.dot(x.T).T)

    # print results
    print()
    print("y dla u1: \n" + str(np.round(y[0][:-1].reshape(3, 3), 2)))
    print()
    print("y dla u2: \n" + str(np.round(y[1][:-1].reshape(3, 3), 2)) + "\n")

    print("weights po backpropagation:")
    print(w_new)

    print("s po backpropagation:")
    print(s_new)
    pass

if __name__ == '__main__':
    main()
