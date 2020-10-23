
import unittest
from collections import deque

class test_is_string_balanced(unittest.TestCase):
    def test_is_string_balanced(self):
        self.assertTrue(is_string_balanced('([])'))
        self.assertFalse(is_string_balanced('([['))
        self.assertFalse(is_string_balanced('([[)'))
        self.assertFalse(is_string_balanced(')'))
        self.assertTrue(is_string_balanced('[[([(())])]]'))

tokens = {
            "(":")",
            "[":"]"
}

def is_open_token(n):
    for i in tokens:
        if n == i:
            return True
    return False

def is_match(open_token, close_token):
    for i in tokens:
        if i == open_token:
            return tokens[i] == close_token
    return False

def is_string_balanced(n):
    myStack = deque()
    for i in n:
        if is_open_token(i):
            myStack.append(i)
        elif len(myStack) == 0 or not is_match(myStack.pop(),i):
            return False
    if len(myStack) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    unittest.main()
    is_string_balanced()

