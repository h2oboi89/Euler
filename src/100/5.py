#! python3


def main():
    n = 2520

    while True:
        if check_value(n):
            return n

        n += 20


def check_value(n):
    for i in range(11, 20):
        if n % i != 0:
            return False

    return True


if __name__ == '__main__':
    print(main())

# 232792560
