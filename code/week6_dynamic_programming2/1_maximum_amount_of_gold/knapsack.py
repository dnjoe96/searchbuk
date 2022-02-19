# Uses python3
import sys

def optimal_weight_false(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result


def optimal_weight(W, wt):

    val = wt
    n = len(val)  # the total individual value. can also be len(wt)
    table = [[0] * (W + 1) for x in range(n + 1)]
    # print(table)
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif wt[i - 1] <= j:
                one = val[i - 1] + table[i - 1][j - wt[i - 1]]
                two = table[i - 1][j]
                table[i][j] = max(one, two)
            else:
                table[i][j] = table[i - 1][j]

    return table[n][W]


# wt = [5, 7, 12, 18]
# W = 20

# res = optimal_weight(W, wt)
# print(res)


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))


