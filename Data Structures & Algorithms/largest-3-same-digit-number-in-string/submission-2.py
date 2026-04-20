class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l =[]
        i = 0
        while i <= len(num)-3:
            if num[i] == num[i+1] and num[i+1] == num[i+2]:
                l.append(num[i:i+3])
                i += 3
                continue
            i += 1

        print(l)
        if len(l) != 0:
            return max(l)
        return ""
            