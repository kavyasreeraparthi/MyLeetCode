class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        def func(dici1, dici2):
            if len(dici1) != len(dici2):
                return False
            for i in dici1:
                if i not in dici2 or dici1[i] != dici2[i]:
                    return False
            return True
        dici1 = {}
        dici2 = {}
        for i in range(len(p)):
            if p[i] in dici2:
                dici2[p[i]] += 1
            else:
                dici2[p[i]] = 1
        n = len(s)
        l = 0
        ans = []
        for r in range(n):
            if s[r] in dici1:
                dici1[s[r]] += 1
            else:
                dici1[s[r]] = 1
            if r-l == len(p):
                if dici1[s[l]] == 1:
                    dici1.pop(s[l])
                else:
                    dici1[s[l]] -= 1
                l += 1
            if r-l+1 == len(p):
                if func(dici1, dici2):
                    ans.append(l)
        return ans
            


            


        