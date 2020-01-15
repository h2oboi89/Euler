#! python3 

import sys, os

def find_path(file):

    triangle = []

    with open(file) as f:
        for l in f:
            parts = l.split()

            r = []

            for p in parts:
                r.append(int(p))

            triangle.append(r)

    triangle.reverse()

    paths = []

    for n in triangle[0]:
        paths.append(Path(n))

    for r in triangle[1:]:
        t = []

        for i in range(len(r)):
            left = paths[i]
            right = paths[i + 1]

            n = r[i]
            p = Path(n)

            if left.sum() > right.sum():
                p.values += left.values
            else:
                p.values += right.values

            t.append(p)

        paths = t

    p = paths[0]
    return p.sum()

class Path(object):
    def __init__(self, n):
        self.values = [n]

    def sum(self):
        return sum(self.values)

    def __str__(self):
        return '[' + ', '.join(map(str, self.values)) + ']'
