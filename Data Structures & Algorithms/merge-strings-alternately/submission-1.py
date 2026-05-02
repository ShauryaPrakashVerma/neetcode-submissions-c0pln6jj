class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer1 = pointer2 = 0

        final_string_list = []

        while pointer1 < len(word1) and pointer2 < len(word2):
            final_string_list.append(word1[pointer1])
            final_string_list.append(word2[pointer2])
            pointer1 += 1
            pointer2 += 1

        if len(word1[pointer1:]):
            final_string_list.append(word1[pointer1:])
        else:
            final_string_list.append(word2[pointer2:])
        
        return "".join(final_string_list)

        