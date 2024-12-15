import unittest

class TestCase2(unittest.TestCase):
    def test_string(self):
        self.assertTrue("hello".islower())

if __name__ == '__main__':
    unittest.main()