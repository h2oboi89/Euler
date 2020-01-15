#! python3

from factorization import primes


def main():
    n = 0

    limit = 10001

    p = []

    while(len(p) < limit):
        n += 1000

        p = primes(n)

    return p[limit - 1]


if __name__ == '__main__':
    print(main())

# 104743
