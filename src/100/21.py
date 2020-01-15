#! python3

from divisors import divisors

def main():
    numbers = []

    amicable_numbers = set()

    for i in range(0, 10000):
        numbers.append(divisors(i))

    for a in range(len(numbers)):
        d_a = sum(numbers[a])

        for b in range(len(numbers)):
            if a == b:
                continue

            d_b = sum(numbers[b])

            if a == d_b and b == d_a:
                amicable_numbers.add(a)
                amicable_numbers.add(b)

    return sum(amicable_numbers)

if __name__ == '__main__':
    print(main())

# 31626