class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for ch in s:
            if ch in mapping:
                if not stack or stack.pop() != mapping[ch]:
                    return False
            else:
                stack.append(ch)
        
        return not stack

        #It must do again because it is fully worked with python3 not familiar with me.
