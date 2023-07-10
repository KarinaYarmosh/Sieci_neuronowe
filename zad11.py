import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def main(a):
    # a = random.uniform(0,12)
    b = random.randint(0, a)
    gcd_f = gcd(a, b)
    if gcd_f > 1:
        print("wieksze > 1: ", gcd_f)
        return 0
    r = 2
    while ((b ** r) - 1) % a == 0:
        r = r + 2
    gcd_plus_1 = gcd(a, b ** (r / 2) + 1)
    gcd_minus_1 = gcd(a, b ** (r / 2) - 1)
    if gcd_plus_1 == 1 and gcd_minus_1 == 1:
        main(a)
    elif gcd_plus_1 > 1 or gcd_minus_1 > 1:
        if gcd_plus_1 > 1:
            print("a - ", a, "b - ", b, "r - ", r)
            print("GCD + 1: ", gcd_plus_1)
        else:
            print("a - ", a, "b - ", b, "r - ", r)
            print("GCD - 1: ", gcd_minus_1)

if __name__ == '__main__':
    main(12)
    print()
    main(91)
    print()
    main(57)
    print()
    main(143)
    print()
    main(1737)
    print()
    main(1859)
    print()
    main(13843)
    print()
    main(988027)
