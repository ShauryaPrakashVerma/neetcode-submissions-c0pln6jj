class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        final = []
        while left <= right:
            if nums[left] ** 2 < nums[right] ** 2:
                final.append(nums[right] ** 2)
                right -= 1
            else:
                final.append(nums[left] ** 2)
                left += 1

        return final[::-1]