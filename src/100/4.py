#! python3


def main():
    a = 999

    maximum = [0, 0, 0]

    while a != 99:
        b = a

        while b != 99:
            n = a * b

            if is_palindrome(n) and n > maximum[2]:
                maximum = [a, b, n]

            b -= 1

        a -= 1

    return maximum[2]


def is_palindrome(num):
    val = str(num)

    for f, r in zip(val, val[::-1]):
        if not f == r:
            return False

    return True


if __name__ == '__main__':
    print(main())

# 906609
