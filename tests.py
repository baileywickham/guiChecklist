import unittest
import checklist

class TestMethods(unittest.TestCase):
    def testColor():
        print(color("hello world", "red"))
        self.assertEqual(input("is the above text red?"), "yes")

if __name__ == '__main__':
    unittest.main() 
