class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l = 0
        temp = []
        for r in range(n):
            if r-l == k:
                l+=1
                temp.append(nums[r]-nums[l])
            if r-l+1 == k:
                temp.append(nums[r]-nums[l])
        return min(temp)