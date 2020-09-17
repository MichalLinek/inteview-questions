class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        output = [[1]]
        for i in range(1, numRows):
            k = [1]
            for j in range(1, i):
                k.append(output[i - 1][j - 1] + output[i - 1][j])
            k.append(1)
            output.append(k)
        return output