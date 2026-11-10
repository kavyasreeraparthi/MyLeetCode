class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        visited = {}
        for i in range(len(nums)):
            current_num = nums[i]
            target_num = target - current_num
            if target_num in visited:
                return [i,visited[target_num]]
            visited[current_num] = i
        return []