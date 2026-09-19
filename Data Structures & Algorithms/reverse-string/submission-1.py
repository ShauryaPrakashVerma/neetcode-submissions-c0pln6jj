class Solution:
    def reverseString(self, s: List[str]) -> None:
        front = 0
        end = len(s) - 1

        while (front < end):

            s[front], s[end] = s[end], s[front]
            front += 1
            end -= 1

        return s