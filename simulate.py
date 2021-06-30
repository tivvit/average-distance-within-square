from random import random


def dist(x, y):
    return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** (1 / 2)


def get_point():
    return random(), random()


def pairs_without_rep():
    points = []
    while True:
        p1 = get_point()
        for p2 in points:
            yield p1, p2
        points.append(p1)


if __name__ == '__main__':
    SAMPLES = 10**8
    sm, ln = 0, 0
    for d in (dist(i, j) for i, j in pairs_without_rep()):
        ln += 1
        sm += d
        if ln == SAMPLES:
            break
    print(f"samples {ln}")
    print(f"average distance is {sm / ln}")
