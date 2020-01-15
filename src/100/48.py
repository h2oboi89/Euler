#! python3

import sys

def main():
    s = 0

    for i in range(1, 1001):
        s += i ** i

    return str(s)[-10:]

if __name__ == '__main__':
    print(main())

# 9110846700
