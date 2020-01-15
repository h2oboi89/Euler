#! python3

import sys, os

def convert(c):
    return ord(c.upper()) - ord('A') + 1

def main():
    names = []

    file = file = os.path.join(sys.path[0], '22_names.txt')

    with open(file) as f:
        content = f.read()

        parts = content.split(',')

        for p in parts:
            names.append(p.replace('"', ''))

    names.sort()

    s = 0

    for n in names:
        v = 0

        for c in n:
            v += convert(c)

        s += (v * (names.index(n) + 1))

    return s

if __name__ == '__main__':
    print(main())

# 871198282