class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        bestending = ans = nums[0]

        for i in range(1, len(nums)):

            choice1 = nums[i] + bestending
            choice2 = nums[i]

            bestending = max(choice1, choice2)
            ans = max(ans, bestending)

        return ans