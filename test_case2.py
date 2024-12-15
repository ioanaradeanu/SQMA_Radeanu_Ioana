import unittest

class TestCase2(unittest.TestCase):
    def test_example2(self):
        self.assertTrue("Hello".isalpha())

if __name__ == '__main__':
    unittest.main()