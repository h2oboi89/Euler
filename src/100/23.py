#! python3

from divisors import divisors

def main():
    abundant_numbers = []

    for i in range(28123):
        if i < sum(divisors(i)):
            abundant_numbers.append(i)

    a_sums = set()

    for a in abundant_numbers:
        for b in abundant_numbers:
            a_sums.add(a + b)

    s = 0
    for i in range(28123):
        if i not in a_sums:
            s += i

    return s

if __name__ == '__main__':
    print(main())

# 4179871