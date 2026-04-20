class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best = ""
        i = 0
        while i <= len(num)-3:
            if num[i] == num[i+1] and num[i+1] == num[i+2]:
                slice = num[i:i+3]
                if slice > best:
                    best = slice
                    i += 3
                    continue
            i += 1

        return best

       
            