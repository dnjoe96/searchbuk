from fibonacci_partial_sum import fibonacci_partial_sum_naive, fibonacci_partial_sum

if __name__ == '__main__':
    # input_n = int(input())
    # input_numbers = [int(x) for x in input().split()]
    import random

    while True:
        from_ = random.randint(0, 10)
        to_ = random.randint(10, 100)

        # print("from:", from_, ", to:", to_)
        # print("fast = ", fibonacci_partial_sum(from_, to_))
        #
        print("from:", from_, ", to:", to_)
        print("normal = ", fibonacci_partial_sum_naive(from_, to_), "fast = ", fibonacci_partial_sum(from_, to_))
        if fibonacci_partial_sum_naive(from_, to_) == fibonacci_partial_sum(from_, to_):
            print("OK")
        else:
            print("wrong")
            break