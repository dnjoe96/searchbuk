# Uses python3
import sys


def get_change_slow(money):
    # write your code here

    if money == 0:
        return 0

    min_number_coins = 10000000
    for i in [4, 3, 1]:
        if money >= i:
            print("entering recursion --- ", money - i)
            num_coins = get_change_slow(money - i)
            if num_coins + 1 < min_number_coins:
                min_number_coins = num_coins + 1

    return min_number_coins


def get_change(money):
    minCoins = [0]*(money + 1)
    coinValueList = [1, 3, 4]
    for cents in range(money + 1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
        minCoins[cents] = coinCount
    return minCoins[money]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))


# print(get_change(10))


