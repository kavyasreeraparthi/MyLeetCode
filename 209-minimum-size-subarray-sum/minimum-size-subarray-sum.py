class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        n = len(nums)
        sum = 0
        ans = float("inf")
        for r in range(n):
            sum += nums[r]
            while sum >= target:
                ans = min(ans, r-l+1)
                sum -= nums[l]
                l += 1
        if ans == float("inf"):
            return 0
        return ans


        