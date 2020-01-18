
import unittest

class test_fizzbuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(1),1)
        self.assertEqual(fizzbuzz(60),"FizzBuzz")
        self.assertEqual(fizzbuzz(69),"Fizz")
        self.assertEqual(fizzbuzz(100),"Buzz")

def fizzbuzz(i):
#    for i in range(1,101):
        if i%3 == 0 and i%5 == 0:
            return "FizzBuzz"
        elif i%3 == 0:
            return "Fizz"
        elif i%5 == 0:
            return "Buzz"
        else:
            return i

if __name__ == '__main__':
    unittest.main()
    fizzbuzz()

