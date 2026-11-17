class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        def atmost(nums,k):
            n = len(nums)
            l = 0
            ans = 0
            odd = 0
            for r in range(n):
                if nums[r] % 2 != 0:
                    odd += 1
                while odd > k:
                    if nums[l] % 2 != 0:
                        odd -= 1
                    l += 1
                ans += r-l+1
            return ans
        return atmost(nums,k)-atmost(nums,k-1)



        