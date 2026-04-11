class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_dict = {}
        for i in nums:
            hash_dict[i] = hash_dict.get(i,0) + 1

        for key, value in hash_dict.items():
            if value > (len(nums)//2):
                return key