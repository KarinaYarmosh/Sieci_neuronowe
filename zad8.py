import numpy as np


def f(x):
    if x < 0:
        return 0
    else:
        return 1

def conv2d(image, kernel, theta=0.0, f=None):
    # Pad image with zeros
    image_padded = np.pad(image, ((1, 1), (1, 1)), mode='constant')

    # Convolve image with kernel
    output = np.zeros_like(image)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if f is None:
                output[x, y] = np.sum(kernel * image_padded[x: x+3, y: y+3]) - theta
            else:
                output[x, y] = f(np.sum(kernel * image_padded[x: x+3, y: y+3]) - theta)

    return output

def average_pooling(image, w, theta=0.0, f=None):
    # Pad image with zeros
    image_padded = np.pad(image, ((1, 1), (1, 1)), mode='constant')

    # Convolve image with kernel
    output = np.zeros_like(image)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if f is None:
                output[x, y] = (np.sum(w * image_padded[x: x + 3, y: y + 3]))
                output[x, y] /= 9
                #output[x, y] -= theta
            else:
                output[x, y] = f((np.sum(w * image_padded[x: x + 3, y: y + 3]) / 9) - theta)

    return output

def main():
    print("Zadanie 1")
    u = np.array([[[0, 0, 0, 0, 0],
                   [0, 1, 1, 1, 0],
                   [0, 1, 0, 1, 0],
                   [0, 1, 1, 1, 0],
                   [0, 0, 0, 0, 0]],

                  [[0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0],
                   [1, 1, 1, 0, 0],
                   [1, 0, 1, 0, 0],
                   [1, 1, 1, 0, 0]],

                  [[0, 0, 0, 0, 0],
                   [0, 0, 1, 1, 1],
                   [0, 0, 1, 0, 1],
                   [0, 0, 1, 1, 1],
                   [0, 0, 0, 0, 0]],

                  [[0, 0, 0, 0, 0],
                   [0, 1, 1, 0, 0],
                   [0, 0, 1, 0, 0],
                   [0, 0, 1, 0, 0],
                   [0, 0, 1, 0, 0]],

                  [[0, 0, 0, 0, 0],
                   [1, 1, 0, 0, 0],
                   [0, 1, 0, 0, 0],
                   [0, 1, 0, 0, 0],
                   [0, 1, 0, 0, 0]]], dtype=np.float64)

    w1 = np.array([[1, 1, 1],
                  [1, 0, 0],
                  [1, 0, 0]], dtype=np.float64)

    w2 = np.array([[1, 1, 1],
                  [1, 1, 1],
                  [1, 1, 1]], dtype=np.float64)

    theta = 2.5

    for i in range(len(u)):
        print(f"y{i+1}\n{conv2d(u[i], w1, theta, f)}")

    print()


    print("Zadanie 2")

    x = np.array([[[0, 1, 0, 0, 0],
                   [0, 0, 1, 0, 0],
                   [0, 1, 0, 0, 0],
                   [0, 0, 1, 0, 0],
                   [0, 1, 0, 0, 0]],

                  [[0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 1],
                   [0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 1],
                   [0, 0, 0, 1, 0]]], dtype=np.float64)

    theta = 2.5/9

    for i in range(len(x)):
        print(f"y{i+1}\n{average_pooling(x[i], w2, theta, f)}")

if __name__ == '__main__':
    main()
