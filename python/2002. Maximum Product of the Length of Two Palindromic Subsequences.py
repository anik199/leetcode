class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        dp = [0] * (1 << n)
        for mask in range(1 << n):
            subseq = ""
            for i in range(n):
                if mask & (1 << i):
                    subseq += s[i]
            if subseq == subseq[::-1]:
                dp[mask] = len(subseq)

        res = 0
        for mask1 in range(1 << n):
            if not dp[mask1]:
                continue
            mask2 = ((1 << n) - 1) ^ mask1
            subset = mask2
            while subset:
                res = max(res, dp[mask1] * dp[subset])
                subset = (subset - 1) & mask2
        return res
