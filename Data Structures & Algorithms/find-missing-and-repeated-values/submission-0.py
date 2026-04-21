class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        final_l =[]
        for l in grid:
            final_l += l
        hash_freq = Counter(final_l)
        print(hash_freq)
        answer = []
        
        for key, value in hash_freq.items():
            if value == 2:
                answer.append(key)
        
        for i in range(len(final_l)):
            if i+1 not in hash_freq.keys():
                answer.append(i+1)
        
        return answer 