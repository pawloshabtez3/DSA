class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        result = []
        for w in words:
            result.append(w[::-1])
        return " ".join(result)
        # The space between the " " is must because it is the space between the words

        