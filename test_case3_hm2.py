import unittest

class TestCase3(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(2 * 3, 6)

if __name__ == '__main__':
    unittest.main()