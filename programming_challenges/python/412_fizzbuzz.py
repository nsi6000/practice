
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


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzbuzz_list = []
        for i in range(1,n+1):
            if (i%5 == 0 and i%3 == 0):
                fizzbuzz_list.append("FizzBuzz")
            elif (i%3 == 0):
                fizzbuzz_list.append("Fizz")
            elif (i%5 == 0):
                fizzbuzz_list.append("Buzz")
            else:
                fizzbuzz_list.append(str(i))
        return fizzbuzz_list
