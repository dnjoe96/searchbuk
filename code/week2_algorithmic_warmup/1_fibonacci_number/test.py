from fibonacci import fib, calc_fib

if __name__ == '__main__':
    # input_n = int(input())
    # input_numbers = [int(x) for x in input().split()]
    import random

    while True:
        input_numbers = random.randint(0, 10)

        print(input_numbers)
        print("normal = ", calc_fib(input_numbers), "fast = ", fib(input_numbers))
        if calc_fib(input_numbers) == fib(input_numbers):
            print("OK")
        else:
            print("wrong")
            break