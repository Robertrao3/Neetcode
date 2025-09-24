class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000}

        res = 0

        for i in range(len(s)):
            curr = roman[s[i]]
            next_val = roman[s[i+1]] if i + 1 < len(s) else 0

            if curr < next_val:
                res -= curr
            else:
                res += curr
        return res