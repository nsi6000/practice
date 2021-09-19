class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n % 2 == 1:
            return False
        else:
            i = 1
            while i < n:
                i *= 2
            return i == n
