class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        major_element = len(nums) // 2

        for num, count in freq.items():
            if count > major_element:
                return num