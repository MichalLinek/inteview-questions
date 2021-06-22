class NumArray:
    def __init__(self, nums):
        n = len(nums)
        self.n = n
        self.tree = [0] * (self.n * 2)
        
        for i in range(n):
            self.tree[i + n] = nums[i]
        for i in range(n - 1, -1, -1):
            self.tree[i] = max(self.tree[i * 2], self.tree[i * 2 + 1])
            
    def update(self, index, val) -> None:
        self.tree[index + self.n] = val
        new_id = (index + self.n) // 2
        while new_id:
            self.tree[new_id] = max(self.tree[new_id * 2],self.tree[new_id *2 + 1])
            new_id = new_id // 2
            
    def maxRange(self, left,right) -> int:
        left += self.n
        right += self.n
        max_v = self.tree[left]
        while left <= right:
            if left % 2 == 1: #right_node
                max_v = max(max_v, self.tree[left])
                left += 1
            if right % 2 == 0: #left_node
                max_v = max(max_v, self.tree[right])
                right -= 1
            left = left // 2
            right = right // 2
        return max_v
        
obj = NumArray([5,84,1,8,3,1])
obj.update(3,51)
print(obj.maxRange(1,3))

