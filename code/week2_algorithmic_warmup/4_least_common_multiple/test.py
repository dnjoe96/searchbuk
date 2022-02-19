from lcm import lcm, lcm_naive
import time

start = time.time()

# your code

# end

print(f'Time: {time.time() - start}')
if __name__ == '__main__':
    # input_n = int(input())
    # input_numbers = [int(x) for x in input().split()]
    import random

    while True:
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)

        # start = time.time()
        print((a, b))
        # print("output = ", lcm_naive(a, b))
        # print("output = ", lcm(714552, 374513))
        # print(f'Time: {time.time() - start}')

        print("normal = ", lcm_naive(a, b), "fast = ", lcm(a, b))
        if lcm(a, b) == lcm_naive(a, b):
            print("OK")
        else:
            print("wrong")

            break