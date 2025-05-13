class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        countVowels = 0
        maxVowels = 0

        for i in range(k):
            if s[i] in vowels:
                countVowels += 1
            maxVowels = countVowels
        
        for i in range(k, len(s)):
            if s[i] in vowels:
                countVowels += 1
            if s[i - k] in vowels:
                countVowels -= 1
            maxVowels = max(maxVowels, countVowels)
        return maxVowels