class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        first_index = -1
        while i <= (len(haystack) - len(needle)):
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    first_index = i
                    break
            
            i += 1
            
        return first_index