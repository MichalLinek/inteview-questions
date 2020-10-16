class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        l = []
        vals = nums + [0]
        curr_l = []
        for id, i in enumerate(vals):
            if i == 0:
                l.append(curr_l)
                curr_l = []
            else:
                curr_l.append(i)
        
        output = 0
        for i in l:
            firstNegativeId = -1
            lastNegativeId = -1
            minusCount = 0
            for id, j in enumerate(i):
                if j < 0:
                    minusCount += 1
                    if firstNegativeId < 0:
                        firstNegativeId = id
                    lastNegativeId = id
                    
            if minusCount % 2 == 0:
                output = max(output, len(i))
            else:
                output = max(output, len(i) - firstNegativeId - 1, lastNegativeId)
        
        return output
    