# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_fast(numbers):
    n = len(numbers)
    # max_product = 0
    max_number = 0
    second_to_max_number = 0
    for first in range(n):
        if numbers[first] > max_number:
            max_number = numbers[first]

    count = 0
    for second in range(n):
        if numbers[second] == max_number:
            count += 1
        if numbers[second] > second_to_max_number and (numbers[second] != max_number or count > 1):
            second_to_max_number = numbers[second]

    max_product = max_number * second_to_max_number
    return max_product


if __name__ == '__main__':
    # input_n = int(input())
    # input_numbers = [int(x) for x in input().split()]
    import random

    while True:
        num = random.randint(0, 10)
        res = [random.randrange(0, 500, 1) for i in range(num)]
        # print(res)
        input_numbers = res
        print(res)
        print("normal = ", max_pairwise_product(input_numbers), "fast = ", max_pairwise_product_fast(input_numbers))
        if max_pairwise_product(input_numbers) == max_pairwise_product_fast(input_numbers):
            print("OK")
        else:
            print("wrong")
            break