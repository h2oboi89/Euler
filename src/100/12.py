#! python3

from divisors import divisors
import math

def main():
    i = 1
    n = 0

    while True:
        n += i

        d = divisors(n)

        if len(d) > 500:
            break

        i += 1

    return n

if __name__ == '__main__':
    print(main())

# 76576500