class Solution:
    def __init__(self):
        self.output = 0
        self.dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start_pos = self.find_start_pos(grid)
        num_of_nodes = sum(i.count(0) for i in grid) + 2
        p = set()
        p.add(start_pos)
        self.recurse(start_pos, p, grid, num_of_nodes)
        return self.output
        
    def recurse(self, current_pos, path_dict, grid, num_of_nodes):
        if grid[current_pos[0]][current_pos[1]] == 2:
            if len(path_dict) == num_of_nodes: self.output += 1
            path_dict.remove(current_pos)
            return
        
        for dir in self.dirs:
            new_pos = (current_pos[0] + dir[0], current_pos[1] + dir[1])
            if self.move_is_valid(new_pos, grid, path_dict):
                path_dict.add(new_pos)
                self.recurse(new_pos, path_dict, grid, num_of_nodes)
        path_dict.remove(current_pos)
                
    def move_is_valid(self, pos, grid, path_dict):
        return pos[0] >= 0 and pos[0] < len(grid) and pos[1] >= 0 and pos[1] < len(grid[0]) and pos not in path_dict and grid[pos[0]][pos[1]] >= 0
    
    def find_start_pos(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return (i, j)