from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_magazine = Counter(magazine)
        hash_ransome_note = Counter(ransomNote)
        flag = True
        for key, value in hash_ransome_note.items():
            if value > hash_magazine[key]:
                flag = False
                break
        
        return flag