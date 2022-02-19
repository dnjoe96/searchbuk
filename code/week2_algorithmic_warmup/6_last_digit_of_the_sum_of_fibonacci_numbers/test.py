from fibonacci_sum_last_digit import fibonacci_sum_naive, fibonacci_sum

if __name__ == '__main__':
    # input_n = int(input())
    # input_numbers = [int(x) for x in input().split()]
    import random

    while True:
        input_numbers = random.randint(0, 100)

        print(input_numbers)
        print("normal = ", fibonacci_sum_naive(input_numbers), "fast = ", fibonacci_sum(input_numbers))
        if fibonacci_sum(input_numbers) == fibonacci_sum_naive(input_numbers):
            print("OK")
        else:
            print("wrong")
            break