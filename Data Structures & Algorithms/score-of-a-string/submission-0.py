class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for index, char in enumerate(s[:-1]):
            sum = sum + abs(ord(s[index]) - abs(ord(s[index+1])))

        return sum

        