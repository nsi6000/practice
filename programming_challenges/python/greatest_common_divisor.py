
import unittest

class test_gcd(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(3,3),3)
        self.assertEqual(gcd(8,12),4)
        self.assertEqual(gcd(16,64),16)
        self.assertEqual(gcd(3,10),1)
        self.assertEqual(gcd(3,15),3)
        self.assertEqual(gcd(24,36),12)

def gcd(x,y):
    if x == y:
        return x
    else:
        while x != y:
            if x < y:
                y = y - x
            else:
                x = x - y
    return x

if __name__ == '__main__':
    unittest.main()
    gcd()

