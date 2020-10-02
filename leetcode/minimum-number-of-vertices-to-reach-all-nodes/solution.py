class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        v = set()
        d = []
        for i in range(n):
            d.append([])
            
        for id, val in enumerate(edges):
            dst = val[0]
            src = val[1]
            d[src].append(dst)
            
        def sort(id):
            v.add(id)
            for dest_node in d[id]:
                if dest_node not in v: sort(dest_node)
            
        for i in range(n):
            for dest in d[i]:
                if dest not in v: sort(dest)
        
        output = []
        for i in range(n):
            if i not in v:
                output.append(i)
        return output
        
        
                
        