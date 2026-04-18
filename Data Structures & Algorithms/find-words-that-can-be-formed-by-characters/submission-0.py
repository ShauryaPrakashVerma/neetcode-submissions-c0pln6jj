class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hash_dict = {}
        for char in chars:
            hash_dict[char] = hash_dict.get(char, 0) + 1

        count = 0
        for word in words:
            hash_char = {}
            for char in word:
                hash_char[char] = hash_char.get(char, 0) + 1
            
            can_form = True
            for key, value in hash_char.items():
                if value > hash_dict.get(key, -1):
                    can_form = False
                    break

            if can_form == True:
                count += len(word)

        return count
            
            