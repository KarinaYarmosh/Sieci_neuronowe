import math


def f(x):
    b = 1.0
    return 1/(1+math.exp(-b*x))

def y(u1, w1, w2, s):
    x1 = f(w1[0]*u1[0]+w1[1]*u1[1]+w1[2]*u1[2])
    x2 = f(w2[0]*u1[0]+w2[1]*u1[1]+w2[2]*u1[2])
    #x3 = f(s[0]*u1[0]+s[1]*u1[1]+s[2]*u1[2])
    return f(s[0]*x1+s[1]*x2+s[2])

def main():
    w1 = [0.0, 1.0, 2.0]
    w2 = [0.0, 1.0, 2.0]
    s1 = [0.0, 1.0, 2.0]
    u1 = [0.0, 0.0, 1.0]
    u2 = [1.0, 0.0, 1.0]
    u3 = [0.0, 1.0, 1.0]
    u4 = [1.0, 1.0, 1.0]
    print("y1: ", y(u1, w1, w2, s1))
    print("y2: ", y(u2, w1, w2, s1))
    print("y3: ", y(u3, w1, w2, s1))
    print("y4: ", y(u4, w1, w2, s1))

if __name__ == '__main__':
    main()