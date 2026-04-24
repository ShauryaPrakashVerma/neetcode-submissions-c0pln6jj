class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_dict = {}
        flag = True
        for index in range(len(s)):
            if s[index] in hash_dict:
                if hash_dict[s[index]] != t[index]:
                    flag = False
            else:
                if t[index] in hash_dict.values():
                    return False
                hash_dict[s[index]] = t[index]

        return flag