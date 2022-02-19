# Uses python3
import sys
import math
import copy


# A class to represent a Point in 2D plane
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# def dist(a, b):
#     # a and b are lists or tuples representing point. a(x1, y1), b(x2, y2)
#     x1, y1 = a[0], a[1]
#     x2, y2 = b[0], b[1]
#
#     c = (x1 - x2) ** 2 + (y1 - y2) ** 2
#     d = math.sqrt(c)
#     return d

# # A utility function to find the
# # distance between two points
def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) *
                     (p1.x - p2.x) +
                     (p1.y - p2.y) *
                     (p1.y - p2.y))


# A Brute Force method to return the
# smallest distance between two points
# in P[] of size n
def bruteForce(P, n):
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if dist(P[i], P[j]) < min_val:
                min_val = dist(P[i], P[j])

    return min_val


# A utility function to find the
# distance beween the closest points of
# strip of given size. All points in
# strip[] are sorted accordint to
# y coordinate. They all have an upper
# bound on minimum distance as d.
# Note that this method seems to be
# a O(n^2) method, but it's a O(n)
# method as the inner loop runs at most 6 times
def stripClosest(strip, size, d):
    # Initialize the minimum distance as d
    min_val = d

    # Pick all points one by one and
    # try the next points till the difference
    # between y coordinates is smaller than d.
    # This is a proven fact that this loop
    # runs at most 6 times
    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y -
                            strip[i].y) < min_val:
            min_val = dist(strip[i], strip[j])
            j += 1

    return min_val


# A recursive function to find the
# smallest distance. The array P contains
# all points sorted according to x coordinate
def closestUtil(P, Q, n):
    # P = x, Q = y
    # If there are 2 or 3 points,
    # then use brute force
    if n <= 3:
        return bruteForce(P, n)

    # Find the middle point
    mid = n // 2
    midPoint = P[mid]

    # Consider the vertical line passing
    # through the middle point calculate
    # the smallest distance dl on left
    # of middle point and dr on right side
    dl = closestUtil(P[:mid], Q, mid)
    dr = closestUtil(P[mid:], Q, n - mid)

    # Find the smaller of two distances
    d = min(dl, dr)

    # Build an array strip[] that contains
    # points close (closer than d)
    # to the line passing through the middle point
    strip = []
    for i in range(n):
        if abs(Q[i].x - midPoint.x) < d:
            strip.append(Q[i])

    # Find the closest points in strip.
    # Return the minimum of d and closest
    # distance is strip[]
    return min(d, stripClosest(strip, len(strip), d))


# The main function that finds
# the smallest distance.
# This method mainly uses closestUtil()
def closest(P, n):
    P.sort(key=lambda point: point.x)
    Q = copy.deepcopy(P)
    Q.sort(key=lambda point: point.y)
    # Use recursive function closestUtil()
    # to find the smallest distance

    return closestUtil(P, Q, n)



def run_func(x, y):
    p = []
    for i in range(0, len(x)):
        point1 = Point(x[i], y[i])
        p.append(point1)

    return p




def minimum_distance(x, y):
    # write your code here

    min_distance = 0
    count = 0
    for i in range(0, len(x)):
        point1 = [x[i], y[i]]
        for j in range(0, len(y)):
            if i == j:
                continue

            point2 = [x[j], y[j]]

            print(point1, point2, min_distance)

            dists = dist(point1, point2)

            if min_distance == 0 and count == 0:
                count += 1
                min_distance = dists
            elif dist <= min_distance and count != 0:
                min_distance = dists
            else:
                continue

    print(round(min_distance, 6))
    #
    # return round(min_distance, 6)


# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#     n = data[0]
#     x = data[1::2]
#     y = data[2::2]
#     print("{0:.9f}".format(minimum_distance(x, y)))


# ans = distance([1, 1], [1, 1])
# print(ans)

# data = list(map(int, ['1', '2', '3', '4', '5', "7", "8", "9", "10"]))
# data = list(map(int, ['2', '0', '0', '3', '4']))
# data = list(map(int, ['4', '7', '7', '1', '100', '4', '8', '7', '7']))
data = list(map(int, ['11', '4', '4', '-2', '-2', '-3', '-4', '-1', '3', '2', '3', '-4', '0', '1', '1', '-1', '-1'
                      , '3', '-1', '-4', '2', '-2', '4']))
n = data[0]
x = data[1::2]
y = data[2::2]

print(n, x, y)

# minimum_distance(x, y)


# Driver code
# P = [Point(2, 3), Point(12, 30),
#      Point(40, 50), Point(5, 1),
#      Point(12, 10), Point(3, 4)]
P = run_func(x, y)
n = len(P)
print("The smallest distance is",
      closest(P, n))