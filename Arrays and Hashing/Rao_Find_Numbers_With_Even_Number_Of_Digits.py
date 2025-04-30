class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            i = len(str(n))
            if i % 2 == 0:
                res += 1
        return res