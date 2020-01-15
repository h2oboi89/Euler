#! python3

from factorization import primes

def rotate(n):
    rotlist = []
    m = str(n)
    counter = 0
    while counter < len(str(n)):
        m = m[1:] + m[0]
        rotlist.append(int(m))
        counter += 1
    return set(rotlist)

def main():
    prime_numbers = primes(1000000)

    circular_primes = set()

    for prime in prime_numbers:
        if prime in circular_primes:
            continue

        prime_permutations = []

        for p in rotate(prime):
            if p in prime_numbers:
                prime_permutations.append(p)
            else:
                prime_permutations = []
                break

        for p in prime_permutations:
            circular_primes.add(p)

    circular_primes = list(circular_primes)
    circular_primes.sort()

    return len(circular_primes)

if __name__ == '__main__':
    print(main())

# 55