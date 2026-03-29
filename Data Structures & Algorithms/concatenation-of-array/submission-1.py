class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = []
        l = len(nums)
        for i in range(l):
            ans.insert(i, nums[i])
        return ans*2
        