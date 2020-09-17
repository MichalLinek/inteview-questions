class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        instr = 4 * instructions
        dirs = [(0,-1), (1, 0), (0, 1), (-1, 0)]
        dir_id = 0
        pos = (0, 0)
        for c in instr:
            curr_dir = dirs[dir_id]
            if c == 'G': pos = (pos[0] + curr_dir[0], pos[1] + curr_dir[1])
            elif c == 'L': dir_id = (dir_id - 1) % 4
            else: dir_id = (dir_id + 1) % 4
        
        return pos == (0, 0)