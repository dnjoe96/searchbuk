import sys

def compute_min_refills(distance, tank, stops):
    # write your code here
    remaining_distance = 400
    # print("distance = ", distance, "tank = ", tank, "stops = ", stops)

    count = 0
    last_stop = 0

    for one in range(len(stops)):
        this_stop = stops[one]
        # print("this_stop:", stops[one], "last_stop:", last_stop)
        if tank >= (this_stop - last_stop):

            final_stop = stops[-1]
            if this_stop != final_stop:
                next_stop = stops[one+1]
                if tank >= (next_stop - last_stop):
                    continue

            if this_stop == final_stop:
                if tank >= remaining_distance:
                    break

            remaining_distance = distance - this_stop
            last_stop = this_stop

            count += 1
            # print("remaining_dist:", remaining_distance)

        else:
            return -1

    if remaining_distance <= tank:
        return count
    return -1


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
