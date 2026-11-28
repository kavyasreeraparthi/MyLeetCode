class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return 0
        nums.sort()
        sum = 0
        for i in range(len(nums)-1):
            sum = max(sum, nums[i+1]-nums[i])
        return sum
