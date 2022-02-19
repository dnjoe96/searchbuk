"""
                **** How The Program works ****
This program find the minimum number of refuels stops before we arrive
at a given destination.
I employed greedy algorithm where I make a stop at the first point at check
if the fuel capacity is sufficient, before hopping to the next stop. And make
This check at each stop.

So at every fuel stop I check if we have sufficient fuel capacity to get to
the next stop. If I do, I keep going, otherwise, I refuel and mark the stop.
And if at a given stop even with refuel, there is still no sufficient capacity
to make the next stop, I end the journey and return -1.
"""
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
    count = 0
    last_stop = 0

    for one in range(len(stops)):
        this_stop = stops[one]
        remaining_distance = distance - this_stop

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
            # print("remaining_dist:", remaining_distance)
        else:
            return -1

    return -1


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    # d, m, stops = 150, 50, [10, 50, 50, 60, 70, 95, 110]
    # d, m, stops = 150, 50, []
    print(compute_min_refills(d, m, stops))
