
import unittest

class test_insertionsort(unittest.TestCase):
    def test_insertionsort(self):
        self.assertListEqual(insertionsort([]),[])
        self.assertListEqual(insertionsort([1]),[1])
        self.assertListEqual(insertionsort([2,1]),[1,2])
        self.assertListEqual(insertionsort([2,3,1]),[1,2,3])
        self.assertListEqual(insertionsort([5,1,4,2,8]),[1,2,4,5,8])

def list_swap(n,x,y):
    n[x], n[y] = n[y], n[x]
    return n

def insertionsort(n):
    if len(n) <= 1:
        return n
    i = 1
    while i < len(n):
        j = i 
        while j > 0 and n[j-1] > n[j]:
            list_swap(n,j,j-1)
            j = j - 1
        i = i + 1
    return n

if __name__ == '__main__':
    unittest.main()
    insertionsort()

