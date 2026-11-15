class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        l = 0
        dici = {}
        n = len(fruits)
        ans = 0
        for r in range(n):
            if fruits[r] not in dici:
                dici[fruits[r]] = 1
            else:
                dici[fruits[r]] += 1
            while len(dici) > 2:
                dici[fruits[l]] -= 1
                if dici[fruits[l]] == 0:
                    dici.pop(fruits[l])
                l += 1
            ans = max(ans, r-l+1)
        return ans
            