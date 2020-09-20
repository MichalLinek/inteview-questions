class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zeros_from_right = [0] * n
        for i in range(n):
            zero_count = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1: break
                zero_count += 1
            zeros_from_right[i] = zero_count
            
        swaps = 0
        for i in range(n):
            if zeros_from_right[i] < n - 1 - i:
                swap_row_id = i + 1
                print(swap_row_id)
                while swap_row_id < n and zeros_from_right[swap_row_id] < n - 1 - i:
                    swap_row_id += 1
                if swap_row_id >= n: return -1
                
                while swap_row_id > i:
                    zeros_from_right[swap_row_id], zeros_from_right[swap_row_id - 1] = zeros_from_right[swap_row_id - 1], zeros_from_right[swap_row_id]
                    swaps += 1
                    swap_row_id -= 1
       
        return swaps