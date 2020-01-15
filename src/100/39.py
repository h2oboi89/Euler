#! python3

from pythagoreanTriples import tripletsWithSum


def main():
    maximum = 0
    max_sum = 0

    for i in range(1, 1000):
        triplets = tripletsWithSum(i)

        if len(triplets) > maximum:
            maximum = len(triplets)
            max_sum = i

    return max_sum


if __name__ == '__main__':
    print(main())

# 840
