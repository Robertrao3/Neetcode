class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1

        for i in range(1, len(nums)):
            if k == 1 or nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k