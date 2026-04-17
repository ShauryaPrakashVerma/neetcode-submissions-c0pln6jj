from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hash = Counter(nums)
        for i in hash.values():
            if i%2 != 0:
                return False
        # if len(nums)%2 == 0:
        return True
        # else:
        #     return False