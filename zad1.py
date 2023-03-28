def f(x):
    if x < 0:
        return 0
    else:
        return 1

def McCullocha_Pittsa(u,w):
    return sum(u[i] * w[i] for i in range(len(u)))

def NOT(w1,w2):
    row1=[0,1]
    row2=[1,1]
    print(f(McCullocha_Pittsa(row1, [w1, w2])))
    print(f(McCullocha_Pittsa(row2, [w1, w2])))

def AND(w1,w2,w3):
    row1=[0,0,1]
    row2=[1,0,1]
    row3=[0,1,1]
    row4=[1,1,1]
    print(f(McCullocha_Pittsa(row1, [w1, w2, w3])))
    print(f(McCullocha_Pittsa(row2, [w1, w2, w3])))
    print(f(McCullocha_Pittsa(row3, [w1, w2, w3])))
    print(f(McCullocha_Pittsa(row4, [w1, w2, w3])))

def NAND(w1,w2,w3):
    row1=[0,0,1]
    row2=[1,0,1]
    row3=[0,1,1]
    row4=[1,1,1]
    print(f(McCullocha_Pittsa(row1, [w1, w2, w3])))
    print(f(McCullocha_Pittsa(row2, [w1, w2, w3])))
    print(f(McCullocha_Pittsa(row3, [w1, w2, w3])))
    print(f(McCullocha_Pittsa(row4, [w1, w2, w3])))

def OR(w1,w2,w3):
    row1=[0,0,1]
    row2=[1,0,1]
    row3=[0,1,1]
    row4=[1,1,1]
    print(f(McCullocha_Pittsa(row1, [w1, w2, w3])))
    print(f(McCullocha_Pittsa(row2, [w1, w2, w3])))
    print(f(McCullocha_Pittsa(row3, [w1, w2, w3])))
    print(f(McCullocha_Pittsa(row4, [w1, w2, w3])))

def main():
    print("Wybierz opcje: ")
    print("1. NOT")
    print("2. AND")
    print("3. NAND")
    print("4. OR")
    wybor = int(input())
    if wybor == 1:
        w1=-2.0
        w2=-1.0
        NOT(w1,w2)
    elif wybor == 2:
        w1=2.0
        w2=2.0
        w3=-3.0
        AND(w1,w2,w3)
    elif wybor == 3:
        w1=-2.0
        w2=-2.0
        w3=3.0
        NAND(w1,w2,w3)
    elif wybor == 4:
        w1=2.0
        w2=2.0
        w3=-1.0
        OR(w1,w2,w3)
    else:
        print("Sprobuj ponownie")
        main()


if __name__ == '__main__':
    main()