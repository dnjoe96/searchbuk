# Uses python3
import sys

# solution - passed
def binary_search(a, x):
    left, right = 0, len(a) - 1
    # write your code here

    # if
    while True:
        mid = (left + right) // 2
        # print(a, a[mid], x, [left, right])

        if a[mid] != x and right == left:
            return -1

        if a[mid] == x:
            # lenth = len(a)
            # print("length = ", lenth * 2)
            return mid

        elif a[mid] < x:
            left, right = mid + 1, right

        elif a[mid] > x:
            left, right = left, mid

    # if a[mid] != x:
    #     return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end=' ')

# l = [1, 5, 8, 12, 13]
# xl = [1, 2, 3, 4, 5]
#
# er = [0, 8, 1, 23, 1, 11]
#
# for x in er:
#     ans = binary_search(l, x)
#     print(ans)
