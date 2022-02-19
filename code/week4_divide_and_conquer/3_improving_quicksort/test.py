
# Uses python3
import sys
import random


def partition3(a, l, r):
    # write your code here

    lt = l  # We initiate lt to be the part that is less than the pivot
    i = l  # We scan the array from left to right
    gt = r  # The part that is greater than the pivot
    pivot = a[l]
    # The pivot, chosen to be the first element of the array, that why we'll randomize the first elements position
    # in the quick_sort function.

    while i <= gt:  # Starting from the first element.
        if a[i] < pivot:
            a[lt], a[i] = a[i], a[lt]
            lt += 1
            i += 1
        elif a[i] > pivot:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1

    return lt, gt


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        print(a)
        return a
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]

    # use partition3
    lt, gt = partition3(a, l, r)

    randomized_quick_sort(a, l, lt - 1)
    randomized_quick_sort(a, gt + 1, r)

    # use partition2
    # m = partition2(a, l, r)
    # randomized_quick_sort(a, l, m - 1)
    # randomized_quick_sort(a, m + 1, r)


A = [6, 6, 3, 7, 8, 2, 1, 0, 5, 7, 4, 8, 0, 34, 55, 12, 1, 5, 3, 4]

# ans = partition3(A, 0, len(A)-1)
# print(ans)

ans2 = randomized_quick_sort(A, 0, len(A) - 1)
print(ans2)
