class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for point1 in range(len(nums)):
            if point1 > 0 and nums[point1] == nums[point1 - 1]:
                continue
                
            point2 = point1 + 1
            point3 = len(nums) - 1
            
            while point2 < point3:
                current_sum = nums[point1] + nums[point2] + nums[point3]
                
                if current_sum == 0:
                    result.append([nums[point1], nums[point2], nums[point3]])
                    point2 += 1
                    point3 -= 1
                    while point2 < point3 and nums[point2] == nums[point2 - 1]:
                        point2 += 1
                    while point2 < point3 and nums[point3] == nums[point3 + 1]:
                        point3 -= 1
                        
                elif current_sum < 0:
                    point2 += 1
                else:
                    point3 -= 1
                    
        return result