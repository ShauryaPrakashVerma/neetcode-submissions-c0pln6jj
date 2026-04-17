class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        else:
            for i in range(len(nums[0:-1])):
                if nums[i]%2 == 0 and nums[i+1] %2 !=0 or nums[i]%2 !=0 and nums[i+1]%2 == 0:
                    continue
                else:
                    return False
            return True
            
