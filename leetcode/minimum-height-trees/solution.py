class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        if n <= 0: return []
        valid_nodes = set(range(n))
        
        d = { }
        for e in edges:
            v1 = e[0]
            v2 = e[1]
            
            if v1 not in d: d[v1] = []
            if v2 not in d: d[v2] = []
            d[v1].append(v2)
            d[v2].append(v1)
        
        bfs = []
        
        for i in d:
            if len(d[i]) == 1:
                bfs.append(i)
        output = []
        while bfs:
            new_bfs = []
            output = bfs
            for i in bfs:
                if len(d[i]) == 0: continue
                dest = d[i][0]
                d[dest].remove(i)
                if len(d[dest]) == 1:
                    new_bfs.append(dest)
            bfs = new_bfs
            
        return output