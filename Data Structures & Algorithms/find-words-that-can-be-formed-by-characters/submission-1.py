class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hash_dict = {}
        count = 0
        hash_dict = Counter(chars)
        for word in words:
            hash_char = Counter(word)
            
            can_form = True
            for key, value in hash_char.items():
                if value > hash_dict.get(key, -1):
                    can_form = False
                    break

            if can_form == True:
                count += len(word)

        return count