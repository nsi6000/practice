
import unittest

class test_fibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0),0)
        self.assertEqual(fibonacci(1),1)
        self.assertEqual(fibonacci(2),1)
        self.assertEqual(fibonacci(3),2)
        self.assertEqual(fibonacci(4),3)
        self.assertEqual(fibonacci(5),5)
        self.assertEqual(fibonacci(6),8)
        self.assertEqual(fibonacci(-5),"wrong input.")


def fibonacci(n):
    if n < 0:
        return "wrong input."
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


if __name__ == '__main__':
    unittest.main()
    fibonacci()

