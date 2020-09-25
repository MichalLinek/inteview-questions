class Solution:
    def minFlips(self, target: str) -> int:
        flips = 0
        last_bulb = '0'
        
        for i in target:
            if i != last_bulb:
                flips += 1
                last_bulb = i
        return flips