#! python3

from fib import fib


def main():
    n = 0
    limit = 4 * 1000 * 1000
    sum = 0

    while True:
        n += 1

        val = fib(n)

        if val >= limit:
            return sum

        if val % 2 == 0:
            sum += val


if __name__ == '__main__':
    print(main())

# 4613732
