#! python3

import math

def main():
    k = 20

    n = 2 * k

    # ( n | k) [n choose k] = n! / ((n - k)! * k!)
    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))

if __name__ == '__main__':
    print(main())

# 137846528820