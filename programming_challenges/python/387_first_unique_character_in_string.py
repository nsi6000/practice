
#O(n^2) solution
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for ci, c in enumerate(s):
            Duplicate = False
            for ni, n in enumerate(s):
                if c == n and ci != ni:
                    Duplicate = True
                    break
            if not Duplicate:
                return ci
        return -1

#O(n) solution with integer list
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_counts = [0]*26
        
        for ci, c in enumerate(s):
            a = ord(c)-ord('a')
            char_counts[a] = char_counts[a] + 1
        
        #for ci, c in enumerate(char_counts):
        #    print(ci, c)
        
        for ci, c in enumerate(s):
            if char_counts[ord(c)-ord('a')] == 1:
                return ci
        
        return -1

#O(n) solution with dictionary
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_counts = {}
        
        for ci, c in enumerate(s):
            if c in char_counts.keys():
                char_counts[c] = char_counts.get(c) + 1
            else:
                char_counts.update({c:1})
        
        #print(str(char_counts))
        
        for ci, c in enumerate(s):
            if char_counts[c] == 1:
                return ci
        
        return -1
