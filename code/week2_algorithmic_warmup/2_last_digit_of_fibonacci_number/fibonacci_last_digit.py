# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):

    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit(n):
    # the key in this algorithm to achieve a lesser runtime is the fact that fibonacci last digits are repeated after 60
    # counts. So the highest number of times I have to go over a is 60 times.
    if n <= 1:
        return n

    previous = 0
    current = 1
    n = n % 60
    # print("new_n = ", n)
    for _ in range(n - 1):
        previous, current = current, previous + current
    # print("current = ", current)
    if current == 1 and n == 0:
        return 0

    return current % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
