import unittest
from factorization import primes, is_prime, factor

class FactorizationTests(unittest.TestCase):
    def test_primes_under_10(self):
        self.assertEqual(primes(10), [2, 3, 5, 7])
    
    def test_primes_under_100(self):
        self.assertEqual(primes(100), [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97])
    
    def test_is_prime(self):
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(2143))

    def test_factor(self):
        self.assertEqual(factor(956873214), [2, 3, 3, 11, 4832693])


if __name__ == '__main__':
    unittest.main()