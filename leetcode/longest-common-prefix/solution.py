class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        if len(strs) == 0 or strs[0] == "": return ""
        for i in range(len(strs[0])):
            letter = strs[0][i]
            for word in strs:
                if len(word) <= i or letter != word[i]: return longest
            longest += letter                
        return longest