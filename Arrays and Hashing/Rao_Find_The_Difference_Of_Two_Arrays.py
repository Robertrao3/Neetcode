class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        diff1 = set()
        diff2 = set()

        for num in nums1:
            if num not in set2:
                diff1.add(num)
        
        for num in nums2:
            if num not in set1:
                diff2.add(num)
        
        return [list(diff1), list(diff2)]