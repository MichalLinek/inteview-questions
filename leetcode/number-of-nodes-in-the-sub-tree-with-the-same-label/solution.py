class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = []
        for i in range(n): graph.append([])
            
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
            
        output = [0] * n
        self.recurse(0, graph, labels, output)
        return output
    
    def recurse(self, nodeNo, graph, labels, output) -> List[int]:
        occTab = [0] * 26
        letterId = ord(labels[nodeNo]) - ord('a')
        occTab[letterId] += 1
        for i in graph[nodeNo]:
            graph[i].remove(nodeNo)
            t2 = self.recurse(i, graph, labels, output)
            occTab = self.sumArrays(occTab, t2)
        
        output[nodeNo] = occTab[letterId]
        return occTab
            
    def sumArrays(self, arr1, arr2):
        o = [0] * 26
        for i in range(26): o[i] = arr1[i] + arr2[i]
        return o