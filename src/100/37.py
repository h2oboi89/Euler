#! python3

from factorization import primes, is_prime

def generate_truncations(i):
    s = str(i)

    for i in range(1, len(s)):
        yield int(s[i:])

    for i in range(1, len(s)):
        yield int(s[:-1 * i])

def main():
    step = 1000000
    limit = 0

    truncatable_primes = []

    prime_numbers = []

    i = 5 # skip the single digit ones
    while len(truncatable_primes) < 11:
        # ensure we don't run out of primes
        if i >= len(prime_numbers):
            limit += step
            prime_numbers = primes(limit, prime_numbers)
            continue

        p = prime_numbers[i]

        truncatable = True
        for t in generate_truncations(p):
            if not is_prime(t, prime_numbers):
                truncatable = False
                break

        if truncatable:
            truncatable_primes.append(p)

        i += 1

    return sum(truncatable_primes)

if __name__ == '__main__':
    print(main())

# 748317