import unittest

class TestMathOperation(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1+1, 2)

class TestAssertions(unittest.TestCase):
    def test_equal(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_boolean(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())

    def test_raises(self):
        s=1
        with self.assertRaises(AttributeError):
            s.split()

if __name__ == '__main__':
    unittest.main()