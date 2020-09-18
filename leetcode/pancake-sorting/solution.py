class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        operations = []
        highest_num_id = len(arr) - 1
        while highest_num_id > 0:
            if arr[highest_num_id] != highest_num_id + 1:
                i = highest_num_id
                id = arr.index(highest_num_id + 1)
                
                operations.append(id + 1)
                arr = arr[id::-1] + arr[id + 1:]
                operations.append(highest_num_id + 1)
                arr = arr[highest_num_id::-1] + arr[highest_num_id + 1:]
                
            highest_num_id -= 1
            
        return operations
        