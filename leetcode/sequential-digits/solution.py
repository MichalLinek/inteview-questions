class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        output = []
        for i in range(1, 10):
            for j in range(1, 10 - i + 1):
                num = 0
                for k in range(i):
                    num = num * 10 + k + j
                if low <= num <= high:
                    output.append(num)
        
        return output