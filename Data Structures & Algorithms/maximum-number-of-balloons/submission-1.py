from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hash_dict = Counter(text)
        b = hash_dict['b']
        a = hash_dict['a']
        l = hash_dict['l'] // 2
        o = hash_dict['o'] // 2
        n = hash_dict['n']
    
        return min(b, a, l, o, n)
