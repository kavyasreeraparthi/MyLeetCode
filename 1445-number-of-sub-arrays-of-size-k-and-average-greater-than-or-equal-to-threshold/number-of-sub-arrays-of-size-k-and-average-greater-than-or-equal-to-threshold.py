class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        n = len(arr)
        l = 0
        ans = []
        val = 0
        count = 0
        for r in range(n):
            if r-l+1 == k:
                val+=arr[r]
                ans.append(val//k)
            elif r-l == k:
                val-=arr[l]
                l+=1
                val+=arr[r]
                ans.append(val//k)
            else:
                val+=arr[r]
        for num in ans:
            if num >= threshold:
                count+=1
        return count

