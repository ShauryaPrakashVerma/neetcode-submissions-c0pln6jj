class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        front = 0
        end = len(s) -1
        print(s[end])
        
        while front <= end:
            s[front], s[end] = s[end], s[front]
            front += 1
            end -= 1

        return s