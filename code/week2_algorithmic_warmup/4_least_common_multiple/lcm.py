# Uses python3
import sys


def lcm_naive(a, b):
    for l in range(max(a,b), a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


def gcd(a, b):
    rem = max(a, b) % min(a, b)
    # print(a, b, rem)
    if rem == 0:
        return min(a, b)
    else:
        new_a = min(a, b)
        return gcd(new_a, rem)


def lcm(a,b):
    return (a * b) // gcd(a, b)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
