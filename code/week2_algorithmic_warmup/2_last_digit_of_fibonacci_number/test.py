from fibonacci_last_digit import get_fibonacci_last_digit_naive, get_fibonacci_last_digit

if __name__ == '__main__':
    # input_n = int(input())
    # input_numbers = [int(x) for x in input().split()]
    import random

    while True:
        input_numbers = random.randint(0, 5000)

        print(input_numbers)
        print("normal = ", get_fibonacci_last_digit_naive(input_numbers), "fast = ", get_fibonacci_last_digit(input_numbers))
        if get_fibonacci_last_digit(input_numbers) == get_fibonacci_last_digit_naive(input_numbers):
            print("OK")
        else:
            print("wrong")

            break