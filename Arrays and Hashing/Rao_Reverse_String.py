class Solution:
    def reverseWords(self, s: str) -> str:

        strsep = s.split()

        reversestr = (strsep[::-1])

        return " ".join(reversestr)