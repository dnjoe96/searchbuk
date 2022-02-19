import sys

def compute_min_refills(distance, tank, stops):
    """ The functions attempts to find the minimum refuel stops at designated 
    fuel stations a vehicle will need to arrive at its destination. And if it
    doesn't, the function returns -1

    Arg:
        distance (int): Total distance of trip
        tank (int): dist a full tank can go
        stops (list): list of stops, values within 0 to distance
    """

    # remaining_distance = 400
    # print("distance = ", distance, "tank = ", tank, "stops = ", stops)

    count = 0
    last_stop = 0

    for one in range(len(stops)):
        this_stop = stops[one]
        remaining_distance = distance - this_stop
        print("this_stop:", stops[one], "last_stop:", last_stop)
        if tank >= (this_stop - last_stop):

            final_stop = stops[-1]
            if this_stop != final_stop:
                next_stop = stops[one + 1]
                if tank >= (next_stop - last_stop):
                    continue
                else:
                    count += 1
                    last_stop = this_stop

            if tank >= remaining_distance:
                return count

            # last_stop = this_stop

            print("remaining_dist:", remaining_distance)

        else:
            return -1

    #if remaining_distance <= tank:
    #    return count
    # return -1


if __name__ == '__main__':
    #d, m, _, *stops = map(int, sys.stdin.read().split())
    d, m, stops = 150, 50, [10, 50, 60, 70, 95]
    print(compute_min_refills(d, m, stops))
