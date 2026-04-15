class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_map = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                smaller_num = stack.pop()
                next_greater_map[smaller_num] = num
            
            stack.append(num)
        return [next_greater_map.get(n, -1) for n in nums1]