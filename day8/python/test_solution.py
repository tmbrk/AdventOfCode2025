import unittest
from solution import solve_part1

class TestDay8(unittest.TestCase):
    def test_part1(self):
        with open('input_test.txt', 'r') as f:
            content = f.read()
        self.assertEqual(solve_part1(content), 40)

if __name__ == '__main__':
    unittest.main()
