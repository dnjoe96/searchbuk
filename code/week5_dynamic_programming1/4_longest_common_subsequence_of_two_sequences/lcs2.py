#Uses python3

import sys


def lcs2(a, b):
    # find the length of the strings
    m = len(a)
    n = len(b)

    # declaring the array for storing the dp values
    block = [[None] * (n + 1) for i in range(m + 1)]

    # print(block)
    for i in range(m + 1):
        for j in range(n + 1):
            # print(i, j)
            if i == 0 or j == 0:
                block[i][j] = 0
            elif a[i - 1] == b[j - 1]:
                # print("a[x] = ", a[i - 1],"b[x] = ", b[j - 1])
                block[i][j] = block[i - 1][j - 1] + 1
            else:
                block[i][j] = max(block[i - 1][j], block[i][j - 1])
            # print(block)

    return block[m][n]



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
#
# a = [2,7,8,3]
# b = [5,2,8,7]
#
# result = lcs2(a, b)
# print(result)