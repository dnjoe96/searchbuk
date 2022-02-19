# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def fibonacci_sum(n):
    # the key in this algorithm to achieve a lesser runtime is the fact that fibonacci last digits are repeated after 60
    # counts. So the highest number of times I have to go over a is 60 times.
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    n = n % 60

    # print("new_n = ", n)
    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current
    # print("current = ", current)
    if current == 1 and n == 0:
        return 0

    return sum % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
