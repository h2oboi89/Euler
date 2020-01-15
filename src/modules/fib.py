from sys import argv

_cache = [0, 1]


def fib(n):
    while n >= len(_cache):
        _cache.append(_cache[-2] + _cache[-1])

    return _cache[n]


def main(argv):
    try:
        n = int(argv[1])
    except (IndexError, ValueError):
        n = 0

    if n < 0:
        n = 0

    print('fib({0}) is {1}'.format(str(n), str(fib(n))))


if __name__ == '__main__':
    main(argv)
