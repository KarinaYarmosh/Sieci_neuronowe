import random
import tensorflow as tf
import numpy as np

def function1(x1,x2,x3):
    return (2*x1**2 + 2*x2**2 + x3 - 2*x1*x2 - 2*x2*x3 - 2*x1 + 3)

def function(X,Y):
    return (3*X**4+4*X**3-12*X**2+12*Y**2-24*Y)

def rand_x_y(N):
    X = tf.Variable(np.random.uniform(-N,N), trainable=True)
    Y = tf.Variable(np.random.uniform(-N,N), trainable=True)
    print("X rand: ", X, " ", "Y rand: ", Y)
    return [X, Y]

def rand_x_y_z(N):
    X = tf.Variable(np.random.uniform(-N,N), trainable=True)
    Y = tf.Variable(np.random.uniform(-N,N), trainable=True)
    Z = tf.Variable(np.random.uniform(-N,N), trainable=True)
    print("X rand: ", X, " ", "Y rand: ", Y, " ", "Z rand (function 1): ", Z)
    return [X, Y, Z]

def main():
    N = 10
    c = 0.01
    X1, Y1, Z1 = rand_x_y_z(N)
    X, Y = rand_x_y(N)
    print("x,", "y")
    for i in range(1):
        optimizer = tf.optimizers.SGD(learning_rate=c, momentum=0.00)
        for i in range(1000):
            optimizer.minimize(lambda: function(X,Y), var_list=[X,Y])
            print((function(X, Y)).numpy(), X.numpy(), Y.numpy(), end="\r")
        print(X.numpy(), Y.numpy(), function(X, Y).numpy())
        X, Y = rand_x_y(N)
    print("x,y,z")
    for i in range(1):
        optimizer = tf.optimizers.SGD(learning_rate=c, momentum=0.00)
        for i in range(1000):
            optimizer.minimize(lambda: function1(X1,Y1, Z1), var_list=[X1,Y1, Z1])
            print((function1(X1, Y1, Z1)).numpy(), X1.numpy(), Y1.numpy(), Z1.numpy, end="\r")
        print(X1.numpy(), Y1.numpy(), Z1.numpy, function1(X1, Y1, Z1).numpy())
        X1, Y1, Z1 = rand_x_y_z(N)

if __name__ == '__main__':
    main()
