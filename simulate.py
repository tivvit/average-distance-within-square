from random import random


def dist(x, y):
    return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** (1 / 2)


def pairs_without_rep(points):
    for i in range(len(points)):
        for j in range(i, len(points)):
            yield points[i], points[j]


if __name__ == '__main__':
    SAMPLES = 10000
    distances = [dist(i, j) for i, j in pairs_without_rep([(random(), random()) for _ in range(SAMPLES)])]
    print(f"samples {len(distances)}")
    print(f"average distance is {sum(distances) / len(distances)}")
