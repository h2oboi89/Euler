#! python3

from factorization import primes
from permute import permute

def convert_to_strings(value):
    return list(map(str, value))

def get_value(digits):
    return int(''.join(digits))

def main():
    prime_numbers = primes(18)

    s = 0
    for permutation in permute(list(range(10))):
        s += test_value(convert_to_strings(permutation), prime_numbers)

    return s

def test_value(digits, prime_numbers):
    p_i = 0

    for i in range(1, len(digits) - 2):
        n = get_value(digits[i:i + 3])

        if n % prime_numbers[p_i] != 0:
            return 0

        p_i += 1

    return get_value(digits)

if __name__ == '__main__':
    print(main())

# 16695334890