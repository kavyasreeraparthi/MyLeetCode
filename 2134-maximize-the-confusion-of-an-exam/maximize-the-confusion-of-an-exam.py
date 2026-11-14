class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l = 0
        ans = 0
        count_t = 0
        count_f = 0
        n = len(answerKey)
        for r in range(n):
            if answerKey[r] == 'T':
                count_t += 1
            elif answerKey[r] == 'F':
                count_f += 1
            while (min(count_t, count_f)) > k:
                if answerKey[l] == 'T':
                    count_t -= 1
                else:
                    count_f -= 1
                l+=1
            ans = max(ans, r-l+1)
        return ans