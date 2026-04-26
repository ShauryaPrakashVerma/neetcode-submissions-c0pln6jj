class Solution:
    def maxScore(self, s: str) -> int:
        max = 0
        for index in range(1,len(s)):
            left = s[0:index]
            right = s[index:]
            left_count = left.count("0")
            right_count = right.count("1")
            if left_count + right_count > max:
                max = left_count + right_count

        return max