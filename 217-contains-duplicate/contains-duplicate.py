class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # O(n**2) approach
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i]==nums[j]:
        #             return True
        # return False
        # O(nlogn) approach
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i]==nums[i+1]:
        #         return True
        # return False
        #Hashmap approach
        # nums_count = Counter(nums)
        # for i in nums:
        #     if nums_count[i]>1:
        #         return True
        # return False
        n = len(nums)
        s = len(set(nums))
        print(n==s)
        if n == s:
            return False
        else:
            return True
        