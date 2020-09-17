class Solution:
    def countAndSay(self, n: int) -> str:
        prev_word = "1"
        for i in range(1, n):
            word = ""
            prev_word += "$"
            counter = 1
            for j in range(1, len(prev_word)):
                if prev_word[j] != prev_word[j - 1]:
                    word += str(counter) + prev_word[j - 1]
                    counter = 1
                else:
                    counter +=1
            prev_word = word
        return prev_word
            