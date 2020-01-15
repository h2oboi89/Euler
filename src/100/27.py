#! python3

from factorization import primes, is_prime

def main():
    primes = []

    answer = []

    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            n = 0

            p = []

            while True:
                d = (n ** 2) + (a * n) + b

                if is_prime(d):
                    p.append(d)
                    n += 1
                else:
                    break

            if len(p) > len(primes):
                primes = p

                answer = [a, b]

    return answer[0] * answer[1]

if __name__ == '__main__':
    print(main())

# -59231