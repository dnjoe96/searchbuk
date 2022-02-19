# Uses python3
import sys


def get_change(m):
    # write your code here
    # implementing greedy algorithm here, my greedy choice is to divide my 10 first, take the integar, and reminder,
    # then reduce the problem to find 5 and 1

    number_of_change = 0

    number_of_ten = m // 10
    remainder_of_ten = m % 10

    # print("number of 10: ", number_of_ten, "number of change: ", number_of_change)
    if number_of_ten > 0 and remainder_of_ten > 0:
        number_of_change += number_of_ten
        # print("number of 10: ", number_of_ten, "number of change: ", number_of_change)
        number_of_five = remainder_of_ten // 5
        remainder_of_five = remainder_of_ten % 5

        number_of_change = number_of_change + remainder_of_five
        # print("number of 1: ", remainder_of_five, "number of change: ", number_of_change)
        if number_of_five > 0:
            number_of_change += number_of_five
            # print("number of 5: ", number_of_five, "number of change: ", number_of_change)

    elif number_of_ten == 0 and remainder_of_ten > 0:
        number_of_five = remainder_of_ten // 5
        remainder_of_five = remainder_of_ten % 5

        number_of_change = number_of_change + remainder_of_five
        if number_of_five > 0:
            number_of_change += number_of_five
        # print("number of 5: ", number_of_five, "number of change: ", number_of_change)
        # print("number of 1: ", remainder_of_five, "number of change: ", number_of_change)

    else:
        return number_of_ten

    return number_of_change


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
