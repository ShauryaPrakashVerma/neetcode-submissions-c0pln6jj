class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hash_dict = {}
        for i in arr:
            hash_dict[i] =  hash_dict.get(i, 0) + 1
        
        max = -1
        for key, value in hash_dict.items():
            if key == value and key > max:
                max = key
        
        return max