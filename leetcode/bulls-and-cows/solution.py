class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secret = list(secret)
        guess = list(guess)
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                guess[i] = "_"
                secret[i] = "_"
                
        for i in range(len(secret)):
            for j in range(len(guess)):
                if secret[i] == "_" or guess[j] == "_": continue
                if secret[i] == guess[j]:
                    cows += 1
                    guess[j] = "_"
                    break
        return str(bulls) +"A" + str(cows) + "B"