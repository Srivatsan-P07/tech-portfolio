import unittest

# Define Test Cases
class TestMathOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)

class TestStringOperations(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("hello".upper(), "HELLO")

    def test_isdigit(self):
        self.assertTrue("123".isdigit())

# Create separate suites
def math_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestMathOperations('test_addition'))
    suite.addTest(TestMathOperations('test_subtraction'))
    return suite

def string_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestStringOperations('test_upper'))
    suite.addTest(TestStringOperations('test_isdigit'))
    return suite

# Combine multiple suites into one
def combined_suite():
    suite = unittest.TestSuite()
    suite.addTests(math_suite())
    suite.addTests(string_suite())
    return suite

if __name__ == '__main__':
    # You can run an individual suite
    print("Running only math_suite:")
    unittest.TextTestRunner().run(math_suite())

    print("\nRunning only string_suite:")
    unittest.TextTestRunner().run(string_suite())

    # Or run all suites combined
    print("\nRunning combined suite:")
    unittest.TextTestRunner().run(combined_suite())