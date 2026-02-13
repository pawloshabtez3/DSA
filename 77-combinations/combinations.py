class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        self.backtrack(1, n, k, [], result)
        return result
    
    def backtrack(self, start, n, k, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        
        for i in xrange(start, n + 1):
            path.append(i)
            self.backtrack(i + 1, n, k, path, result)
            path.pop()
        