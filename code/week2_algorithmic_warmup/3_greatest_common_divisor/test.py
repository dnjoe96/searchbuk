from gcd import gcd, gcd_naive

if __name__ == '__main__':
    # input_n = int(input())
    # input_numbers = [int(x) for x in input().split()]
    import random

    while True:
        a = random.randint(1, 5000)
        b = random.randint(1, 5000)

        print((a, b))
        print("normal = ", gcd_naive(a, b), "fast = ", gcd(a, b))
        if gcd_naive(a, b) == gcd_naive(a, b):
            print("OK")
        else:
            print("wrong")

            break