class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort()
        ans = 0
        n = len(cost)
        for i in range(n-1,-1,-3):
            ans += cost[i]
            j = i-1
            if j>=0:
                ans += cost[j]
        return ans