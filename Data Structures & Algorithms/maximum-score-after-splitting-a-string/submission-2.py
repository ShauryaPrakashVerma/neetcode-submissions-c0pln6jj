class Solution:
    def maxScore(self, s: str) -> int:
        zeroes_left = 0
        ones_right = s.count("1")
        max_sum = 0

        for index in range(len(s)-1):
            if s[index] == "0":
                zeroes_left += 1
            else:
                ones_right -= 1
            
            max_sum = max(max_sum, zeroes_left + ones_right)

        return max_sum