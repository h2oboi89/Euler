#! python3

from fractions import Fraction

def get_digits(n):
    return [int(i) for i in str(n)]

def do_digits_match(a, b):
    for i, d_a in enumerate(a):
        for j, d_b in enumerate(b):
            if d_a == d_b:
                return i, j
    return -1, -1

def main():
    results = []

    for i in range(11, 100):
        if i % 10 == 0:
            continue

        for j in range(11, i):
            if j % 10 == 0:
                continue

            # print('{} / {}'.format(j, i), end=' ')

            i_digits = get_digits(i)
            j_digits = get_digits(j)

            d_i, d_j = do_digits_match(i_digits, j_digits)

            if d_i != -1:
                a = j / i

                del i_digits[d_i]
                del j_digits[d_j]

                k = i_digits[0]
                l = j_digits[0]

                b = l / k

                if a == b:
                    results.append(Fraction(l, k))

    result = 1
    for f in results:
        result *= f

    return result.denominator

if __name__ == '__main__':
    print(main())

# 100