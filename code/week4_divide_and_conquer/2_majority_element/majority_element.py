# Uses python3
import sys

# solution - passed
def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    # write your code here
    limit = right//2
    dict = {}
    for x in a:
        # print(dict)
        if x not in dict.keys():
            dict[x] = 1
        else:
            dict[x] = dict[x] + 1
        if dict[x] > limit:
            return dict[x]
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

# a = [1, 2, 3, 4, 5]
# l = 0
# r = len(a)
#
# test = get_majority_element(a, l, r)
#
# print(test)