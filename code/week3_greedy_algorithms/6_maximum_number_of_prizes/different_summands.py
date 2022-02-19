# Uses python3
import sys


def optimal_summands(n):
    summands = []
    # write your code here

    # initialize number to start from 1
    num = 1

    # initialize the sum from zero
    sum = 0

    # while our computed sum doesn't exceed the given sum
    while sum < n:
        # add
        sum += num

        # append the number to list
        summands.append(num)

        # increment number by 1
        num = num + 1

        # if we get to the point where the difference is less than new number, add the difference to the
        # last number we appended to the list
        if n - sum < num:
            summands[-1] += n - sum

            break
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')


# summands = optimal_summands(9)
# print(summands)
