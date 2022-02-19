# Uses python3
def calc_fib(n):

    if n <= 1:
        return n
    else:

        f1 = 0
        f2 = 1
        for x in range(n - 1):
            # print(f1, f2)
            f1, f2 = f2, f2 + f1
        return f2

n = int(input())
print(calc_fib(n))
