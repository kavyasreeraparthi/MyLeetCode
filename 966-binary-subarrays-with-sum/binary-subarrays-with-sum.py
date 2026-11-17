class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def atmost(nums,goal):
            if goal<0:
                return 0
            l = 0
            n = len(nums)
            ans = 0
            temp = 0
            for r in range(n):
                temp += nums[r]
                while temp > goal:
                    temp -= nums[l]
                    l += 1
                ans += r-l+1
            return ans
        return atmost(nums,goal)-atmost(nums,goal-1)

