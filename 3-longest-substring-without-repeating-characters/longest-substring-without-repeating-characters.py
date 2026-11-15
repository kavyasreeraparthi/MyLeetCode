class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        temp = []
        ans = 0
        for r in range(n):
            while s[r] in temp:
                temp.pop(0)
            temp.append(s[r]) 
            ans = max(ans, len(temp))
        return ans