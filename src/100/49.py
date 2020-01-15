#! python3

from factorization import primes, is_prime
from permute import permute

def main():
    prime_numbers = primes(10000)

    prime_numbers = [p for p in prime_numbers if p > 999]

    permutations = []

    for p in prime_numbers:
        t = set() # numbers with non-unique digits should be ignored

        for perm in permute(p):
            i = int(''.join(map(str, perm)))

            if i < 1000:
                continue

            if is_prime(i):
                if i in prime_numbers:
                    prime_numbers.remove(i)
                t.add(i)

        if len(t) > 2:
            t = list(t)
            t.sort()
            permutations.append(t)

    j = 0
    for perm in permutations:
        t = set()
        for i in range(len(perm) - 1):
            for p in perm[i + 1:]:
                if p - perm[i] == 3330:
                    t.add(perm[i])
                    t.add(p)

        if len(t) == 3:
            if j == 1:
                return int(''.join(map(str, t)))
            j += 1

if __name__ == '__main__':
    print(main())

# 296962999629