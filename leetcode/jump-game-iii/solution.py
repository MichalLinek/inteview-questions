class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        return self.recurse(arr, start, set())
    def recurse(self, arr, i, visited):
        if i < 0 or i >= len(arr): return False
        if arr[i] == 0: return True
        if i in visited: return False
        
        visited.add(i)
        return self.recurse(arr, i + arr[i], visited) or self.recurse(arr, i - arr[i], visited)