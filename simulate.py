from random import random
from statistics import mean
from itertools import permutations


def dist(points):
    x, y = points
    return (abs(x[0] - y[0]) ** 2 + abs(x[1] - y[1])) ** (1 / 2)


if __name__ == '__main__':
    SAMPLES = 10000
    points = [(random(), random()) for _ in range(SAMPLES)]
    distances = map(dist, permutations(points, 2))
    print(f"average distance is {mean(distances)}")
