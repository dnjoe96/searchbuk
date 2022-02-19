#Uses python3

import sys

def three_digit(num):
    strn = "%04d" %(num)
    return strn

def compare_four_digits(num1, num2):
    str1 = "%d" % (num1)
    str2 = "%d" % (num2)

    # for n in range(4):
    #     if str1[n] > str2[n]:
    #         return str1

    if len(str1) > len(str2):
        if str(num1)[0] > str(num2):
            maxe = num2

    elif len(str1) < len(str2):
        if str(num1)[0] < str(num2):
            maxe = num1

    else:
        maxe = 0

    return maxe

def largest_number(a):
    #write your code here
    ans = ""

    while len(a) != 0:
        print(a)
        max_digit = 0
        for d in a:
            # if str(d) >= int(max_digit):
            if int(d) >= int(max_digit):
                max_digit = str(d)
        ans += max_digit
        a.remove(int(max_digit))
    return ans

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = input.split()
#     a = data[1:]
#     print(largest_number(a))

# a = [23, 56, 67, 6]
# print(largest_number(a))

# print(three_digit(10))
# print(largest_number([3, 23]))

print(compare_four_digits(3, 23))