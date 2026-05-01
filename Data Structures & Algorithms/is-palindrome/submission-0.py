class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s.replace(" ","")

        list_t = list(t)
        new_list = []
        for char in list_t:
            if char.isalnum():
                new_list.append(char.lower())
            else:
                continue

        left = 0
        right = len(new_list) - 1

        while left <= right:
            if new_list[left] != new_list[right]:
                return False
            left += 1
            right -= 1
        
        return True
        
        



