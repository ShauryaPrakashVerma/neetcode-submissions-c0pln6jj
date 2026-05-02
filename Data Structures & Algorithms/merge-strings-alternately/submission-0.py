class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        small = 0
        big = 0
        if len(word1) < len(word2):
            small = word1
            big = word2
        else:
            small = word2
            big = word1

        list_final = []
        pointer = 0
        for index in range(len(small)):
            list_final.append(word1[index])
            list_final.append(word2[index])
            pointer += 1

        return "".join(list_final) + big[pointer:]


        