import unittest
from search import binary_search

class SearchTests(unittest.TestCase):
    def test_binary_search_empty(self):
        self.assertEqual(binary_search([], 0), -1)

    def test_binary_search_non_empty(self):
        for i in range(1, 5):
            key = i - 1
            self.assertEqual(binary_search(range(i), key), key)

    def test_binary_search_not_found(self):
        values = [1, 2, 3, 4, 5]

        self.assertEqual(binary_search(values, -1), -1)

if __name__ == '__main__':
    unittest.main()