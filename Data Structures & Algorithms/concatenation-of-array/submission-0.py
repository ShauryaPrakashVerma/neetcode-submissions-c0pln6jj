class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = []
        print(len(nums))
        for i in range(len(nums)):
            ans.insert(i, nums[i])
        return ans*2
        