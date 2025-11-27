import math

class Solution(object):
    def minOperations(self, k):
        best = 10**18
        r = int(math.sqrt(k))

        # Try small x up to sqrt(k)
        for x in range(1, r + 1):
            f = x + int(math.ceil(float(k) / x))
            if f < best:
                best = f

        # Try x from quotient buckets
        for t in range(1, r + 1):
            x = k // t
            if x >= 1:
                f = x + int(math.ceil(float(k) / x))
                if f < best:
                    best = f

        return best - 2

# Tests
print Solution().minOperations(11)  # Expected 5
print Solution().minOperations(5)   # Expected 4
print Solution().minOperations(20)  # Expected 6
