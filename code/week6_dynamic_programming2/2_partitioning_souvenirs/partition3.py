# Uses python3
import sys
import itertools

def partition3_(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0


def partition3(A):
    total = sum(A)
    if len(A) < 3 or total % 3:  # 1
        return 0
    
    third = total // 3
    table = [[0] * (len(A) + 1) for x in range(third + 1)]  # 2

    for i in range(1, third + 1):
        for j in range(1, len(A) + 1):  # 3
            hold = i - A[j - 1]  # 4
            if A[j - 1] == i or (hold > 0 and table[hold][j - 1]):  # 5
                table[i][j] = 1 if table[i][j - 1] == 0 else 2
            else:
                table[i][j] = table[i][j - 1]  # 6

    if table[-1][-1] == 2:
        return 1
    else:
        return 0
    

# vl = [17, 59, 34, 57, 17, 23, 67, 1, 18, 2, 59]
# vl = [1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]
# vl = [40]
# vl = [3,3,3,3]
# res = solution(vl)
#
# print(res)
# #
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

