class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash_dict = {}
        for key, value in enumerate(nums):
            hash_dict[value] = hash_dict.get(value, 0) + 1
        l = []
        for value, freq in hash_dict.items():
            if freq > (len(nums)//3):
                l.append(value)

        return l