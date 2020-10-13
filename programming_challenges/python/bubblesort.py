
import unittest

class test_bubblesort(unittest.TestCase):
    def test_bubblesort(self):
        self.assertListEqual(bubblesort([]),[])
        self.assertListEqual(bubblesort([1]),[1])
        self.assertListEqual(bubblesort([2,1]),[1,2])
        self.assertListEqual(bubblesort([2,3,1]),[1,2,3])
        self.assertListEqual(bubblesort([5,1,4,2,8]),[1,2,4,5,8])

def list_swap(n,x,y):
    n[x], n[y] = n[y], n[x]
    return n

def bubblesort(n):
    swapped = True 
    if len(n) <= 1:
        return n
    while swapped:
        swapped = False
        for i in range(len(n)-1):
            if n[i] > n[i+1]:
                swapped = True
                list_swap(n,i,i+1) 
    return n

if __name__ == '__main__':
    unittest.main()
    bubblesort()

