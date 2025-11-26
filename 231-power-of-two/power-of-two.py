class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n > 1: #if it is 0 the loop doesnt stop so it should be 1 to stop at 1 and output True
            if n % 2 != 0:
                return False
            n = n / 2
        return True
        
        