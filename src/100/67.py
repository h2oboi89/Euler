#! python3

from triangle import find_path

import sys, os

def main():
    file = os.path.join(sys.path[0], '67_triangle.txt')

    return find_path(file)

if __name__ == '__main__':
    print(main())

# 7273
