class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hash_freq = Counter(arr)
        print(hash_freq)
        count = 0
        for key, value in hash_freq.items():
            if value == 1:
                count += 1
                if count == k:
                    return key
        return ""