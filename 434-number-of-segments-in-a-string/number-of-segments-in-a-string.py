class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        sections = s.split(" ")
        return sum(1 for p in sections if p != "")
        