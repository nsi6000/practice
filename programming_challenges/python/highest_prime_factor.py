
import unittest

class test_hpf(unittest.TestCase):
    def test_hpf(self):
        self.assertEqual(hpf(2),2)
        self.assertEqual(hpf(12),3)
        self.assertEqual(hpf(124),31)
        self.assertEqual(hpf(3453),1151)

def hpf(x):
    if x == 2:
        return x
    else:
        d = 2
        while x != 0:
            if x % d != 0:
                d = d + 1
            else:
                hpf = x
                x = x / d
                if x == 1:
                    return hpf

if __name__ == '__main__':
    unittest.main()
    hpf()

