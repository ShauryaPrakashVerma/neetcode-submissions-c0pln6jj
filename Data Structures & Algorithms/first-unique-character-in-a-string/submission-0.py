class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_freq = Counter(s)

        for index, value in enumerate(s):
            if hash_freq[value] == 1:
                return index

        return -1


