class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = 0
        char_dict = {}
        for word in words:
            for char in word:
                char_dict[char] = char_dict.get(char,0) + 1
        
        for i in char_dict.values():
            if i%len(words):
                return False
        return True