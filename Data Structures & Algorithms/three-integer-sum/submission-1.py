class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)-2):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue 

            left = i + 1
            right = len(nums) - 1
            sum = -1 * nums[i]

            while left < right:
                if nums[left] + nums[right] == sum:
                    # move both
                    result.append([nums[i] , nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < len(nums) and nums[left] == nums[left-1]:
                        left += 1
                    
                    while right > len(nums) and nums[right] == nums[right + 1]:
                        right -= 1
                
                elif nums[left] + nums[right] < sum:
                    # Move left pointer forward
                    left += 1

                else:  # nums[left] + nums[right] > sum
                    right -= 1

        return result