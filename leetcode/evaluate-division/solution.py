class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(values)
        a_dict = {}
        for i in range(n):
            first = equations[i][0]
            second = equations[i][1]
            
            value = values[i]
            
            if first not in a_dict: a_dict[first] = [(first, 1)]
            if second not in a_dict: a_dict[second] = [(second, 1)]
                
            a_dict[first].append((second, value))
            a_dict[second].append((first, 1 / value))
            
        output = []
        for i in queries:
            val = -1
            if i[0] in a_dict and i[1] in a_dict: 
                s = set()
                s.add(i[0])
                val = self.dfs(i[0], i[1], 1, a_dict, s)
            output.append(val)
        return output
                
    def dfs(self, start, end, value, a_dict, s_visited):
        if start == end: return value
        
        nodes = a_dict[start]
        
        for next_node, weight in nodes:
            if next_node in s_visited: continue
            s_visited.add(next_node)
            output = self.dfs(next_node, end, value * weight, a_dict, s_visited)
            if output > -1:
                return output
            s_visited.remove(next_node)
        return -1 
        
        
            