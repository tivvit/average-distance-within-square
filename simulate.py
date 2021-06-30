from random import random
from statistics import mean
from itertools import permutations


def dist(points):
    x, y = points
    return (abs(x[0] - y[0]) ** 2 + abs(x[1] - y[1])) ** (1 / 2)


def pairs_without_rep(points):
    for i in range(len(points)):
        for j in range(i, len(points)):
            yield points[i], points[j]


if __name__ == '__main__':
    SAMPLES = 10000
    points = ((random(), random()) for _ in range(SAMPLES))
    distances = map(dist, pairs_without_rep(points))
    print(f"average distance is {mean(distances)}")
