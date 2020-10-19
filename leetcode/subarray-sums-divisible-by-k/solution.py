class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        pref_sum = 0
        d = [0] * K
        d[0] = 1
        for i in range(len(A)):
            pref_sum = (pref_sum + A[i]) % K
            d[pref_sum] += 1
                
        output = 0
        for i in range(K):
            output += (d[i] * (d[i] - 1)) // 2
        print(d)
        return output