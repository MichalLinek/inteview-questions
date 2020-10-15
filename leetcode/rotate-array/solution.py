class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        counter = 0
        n = len(nums)
        for i in range(k):
            prev_num = nums[i]
            id = (i + k) % n
            while id != i:
                prev_num, nums[id] = nums[id], prev_num
                id  = (id + k) % n
                counter += 1
            nums[i] = prev_num
            counter += 1
            if counter == n: break
        