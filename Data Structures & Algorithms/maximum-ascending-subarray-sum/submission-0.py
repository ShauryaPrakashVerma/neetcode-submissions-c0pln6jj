class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sum = nums[0]
        max_sum = nums[0]
        last_visited = nums[0]
        for index in range(1,len(nums)):
            if nums[index] > last_visited:
                sum += nums[index]
            else:
                if sum > max_sum:
                    max_sum = sum
                sum = nums[index]
            
            last_visited = nums[index]
        
        if sum > max_sum:
            max_sum = sum
            
        return max_sum