#! python3


def squareOfSum(val):
    t = (val * (val + 1)) // 2

    return t * t


def sumOfSquares(val):
    return (val * (val + 1) * (2 * val + 1)) // 6


def main():
    return squareOfSum(100) - sumOfSquares(100)


if __name__ == '__main__':
    print(main())

# 25164150
