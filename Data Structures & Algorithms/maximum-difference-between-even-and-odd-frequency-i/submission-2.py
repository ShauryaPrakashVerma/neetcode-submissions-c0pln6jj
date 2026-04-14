class Solution:
    def maxDifference(self, s: str) -> int:
        
        '''
        c = Counter(s)
        maxOdd = max(x for x in c.values() if x % 2 == 1)
        minEven = min(x for x in c.values() if x % 2 == 0)
        return maxOdd - minEven
        '''
        hash_dict = {}
        for char in s:
            hash_dict[char] = hash_dict.get(char, 0) + 1
        
        odd_freq = []
        even_freq = []
        for freq in hash_dict.values():
            if freq % 2 == 0:
                even_freq.append(freq)
            else:
                odd_freq.append(freq)

        return max(odd_freq) - min(even_freq)