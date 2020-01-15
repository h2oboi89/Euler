#! python3

from pythagoreanTriples import tripletsWithSum


def main():
    # problem tells us there is only 1
    triplet = tripletsWithSum(1000)[0]

    result = 1

    for i in triplet:
        result *= i

    return result


if __name__ == '__main__':
    print(main())

# 31875000
