#! python3

from factorization import primes

import time

def main():
    prime_numbers = primes(1000000000)

    maximum = 0

    for p in prime_numbers:
        digits = []

        t = p
        while t != 0:
            digits.append(t % 10)
            t //= 10

        digits.sort()

        i = 1
        pandigital = True
        for d in digits:
            if d != i:
                pandigital = False
                break
            i += 1

        if pandigital:
            if p > maximum:
                maximum = p

    return maximum


if __name__ == '__main__':
    start_time = time.time()
    print(main())
    print("--- %s seconds ---" % (time.time() - start_time))
