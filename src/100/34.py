#! python3

from math import factorial

factorials = [factorial(i) for i in range(0, 10)]

def findUpperBound():
    # running this shows that we can stop once we hit 8 digit numbers
    n = 99
    s = 999

    i = len(str(n))
    while len(str(n)) < len(str(s)):
        n += 9 * 10 ** i

        i += 1

        s = factorials[9] * len(str(n))

    return factorials[9] * i

def main():
    s = 0

    for n in range(10, findUpperBound()):
        tmp = n
        total = 0
        while tmp > 0:
            total += factorials[tmp % 10]
            tmp //= 10

        if total == n:
            s += n

    return s

if __name__ == '__main__':
    print(main())

# 40730