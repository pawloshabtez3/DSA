class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        cleaned = s.strip()
        words = cleaned.split()
        words = words[::-1]
        result = " ".join(words)
        return result

        