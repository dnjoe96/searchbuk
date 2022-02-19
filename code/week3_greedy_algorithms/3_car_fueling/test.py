from car_fueling import compute_min_refills

if __name__ == '__main__':
    # input_n = int(input())
    # input_numbers = [int(x) for x in input().split()]
    import random
    import sys

    # print(compute_min_refills(950, 400, [250, 375, 550, 750]))
    print("6", compute_min_refills(6, 3, [2, 3, 4]))
    # ans = 1
    print("7", compute_min_refills(7, 3, [1, 2, 3, 4, 5, 6]))
    # ans = 2
    print("7", compute_min_refills(7, 3, [1, 2, 6]))
    # ans = -1
    print("12", compute_min_refills(12, 3, [1, 2, 4, 5, 6, 7, 8, 10, 11]))
    # ans = 4
    print("12", compute_min_refills(12, 3, [1, 2, 4, 5, 8, 9, 10, 11]))
    # ans = 4
    print("900", compute_min_refills(900, 400, [200, 350, 550, 750]))
    # ans = 2
    print("10", compute_min_refills(10, 3, [1, 2, 5, 9]))
    # ans = -1
    print("1000", compute_min_refills(1000, 200, [100, 150, 180, 250, 300, 350, 500, 650, 850]))
    # ans = -1

    # while True:
        # input_numbers = random.randint(0, 10)
        # d = int(random.randint(1, 10e5))
        # m = int(random.randint(1, 400))
        # _ = int(random.randint(1, 400))
        # stops = []
        # ini = 0
        # for x in range(_):
        #     stops.append(random.randint())
        # d, m, _, *stops = map(int, sys.stdin.read().split())
        # print(compute_min_refills(d, m, stops))

        # print(input_numbers)
        # print("normal = ", calc_fib(input_numbers), "fast = ", fib(input_numbers))
        # if calc_fib(input_numbers) == fib(input_numbers):
        #     print("OK")
        # else:
        #     print("wrong")
        #     break