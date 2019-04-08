# python3
import sys


def compute_min_refills(distance, tank, stops):
    stops = sorted(stops)
    stops.append(distance)

    last_stop = 0
    number_of_stops = 0

    for i, stop in enumerate(stops):
        if (stop - stops[i-1]) > tank:
            return -1

        if tank < (stop - last_stop):
            number_of_stops += 1
            last_stop = stops[i-1]

    return number_of_stops


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    # d, m, stops = 500, 200, [100, 200, 300, 400]
    print(compute_min_refills(d, m, stops))

