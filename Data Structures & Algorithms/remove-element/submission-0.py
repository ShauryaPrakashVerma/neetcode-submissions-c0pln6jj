class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = []
        for i in nums:
            if i == val:
                continue
            r.append(i)
        for i in range(len(r)):
            nums[i] = r[i]
        return len(r) 