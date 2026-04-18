class Solution:
    def countCharacters(self, words, chars):
        total = 0
        for word in words:
            good = True
            for c in word:
                if word.count(c) > chars.count(c):
                    good = False
                    break
            if good:
                total += len(word)
        return total
