class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count = {}

        for c in magazine:
            count[c] = 1 + count.get(c, 0)
        
        for c in ransomNote:
            if c in count and count[c] > 0:
                count[c] -= 1
            else:
                return False
        return True