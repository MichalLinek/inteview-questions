class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ones = set()
        zeros = set()
        visited = set()
        first = ""
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    ones.add(str(r) + "," + str(c))
                    first = str(r) + "," + str(c)
                else:
                    zeros.add(str(r) + "," + str(c))
                    
        l = [first]
        visited.add(first)
        perimeter = 0
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while l:
            curr_one = l.pop()
            
            row, col = [int(i) for i in curr_one.split(",")]
            
            for d in dirs:
                new_r = d[0] + row
                new_c = d[1] + col
                
                new_key = str(new_r) + "," + str(new_c)
                if new_key in ones and new_key not in visited:
                    l.append(new_key)
                    visited.add(new_key)
                if new_key not in ones:
                    perimeter +=1
                    
                    
        
        return perimeter