import unittest
import random

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

class TestSetUp(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.class_random_number = random.randint(1,100)

    def setUp(self):
        self.test_random_number = random.randint(1,100)

    def test_classes1(self):
        print()
        print('SetUpClass variable: ',self.class_random_number)
        print('SetUp Variable: ',self.test_random_number)

    def test_classes2(self):
        print()
        print('SetUpClass variable: ',self.class_random_number)
        print('SetUp Variable: ',self.test_random_number)

    def tearDown(self):
        print('teardown')
    
    @classmethod
    def tearDownClass(cls):
        print('------------------')
        print('TearDown Class')

if __name__ == '__main__':
    unittest.main()