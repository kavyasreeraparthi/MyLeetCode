class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def atmost(nums,k):
            l = 0
            n = len(nums)
            ans = 0
            temp = 0
            dici = {}
            for r in range(n):
                if nums[r] not in dici:
                    dici[nums[r]] = 1
                else:
                    dici[nums[r]] += 1
                while len(dici) > k:
                    if dici[nums[l]] == 1:
                        dici.pop(nums[l])
                    else:
                        dici[nums[l]] -= 1
                    l += 1
                ans += r-l+1
            return ans
        return atmost(nums,k)-atmost(nums,k-1)
        