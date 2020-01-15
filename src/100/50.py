#! python3

import sys
import os

root = os.path.dirname(os.path.abspath(os.pardir))

sys.path.insert(0, root)
sys.path.insert(0, root + '/Factorization')

from factorization import primes
from search import binary_search

def main():
    limit = 1000000

    prime_numbers = primes(limit)

    prime_sums = [0]

    for prime_number in prime_numbers:
        prime_sum = prime_sums[-1] + prime_number

        if prime_sum < limit:
            prime_sums.append(prime_sum)
        else:
            break

    chain_length = -1
    result = -1

    for prime_sum in prime_sums[::-1]:
        index_adjustment = 0
        index = binary_search(prime_sums, prime_sum)

        for prime_number in prime_numbers:
            if binary_search(prime_numbers, prime_sum) != -1:
                current_chain_length = index - index_adjustment

                if current_chain_length > chain_length:
                    chain_length = current_chain_length
                    result = prime_sum

                if current_chain_length < chain_length:
                    break
            else:
                prime_sum = prime_sum - prime_number

                index_adjustment += 1

                if prime_sum < 0 or index - index_adjustment < chain_length:
                    break

    return result

def test():
    answer = main()
    print(answer)
    return answer == 997651

if __name__ == '__main__':
    print(main())
