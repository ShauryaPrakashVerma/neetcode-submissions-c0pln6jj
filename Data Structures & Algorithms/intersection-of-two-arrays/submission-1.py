class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert the smaller list to a set to save space
        set1 = set(nums1)
        res = set()
        
        for num in nums2:
            if num in set1:  # This lookup is now O(1) instead of O(m)
                res.add(num)
                
        return list(res)