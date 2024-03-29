class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        pali = {} #mask : length
        
        for mask in range(1, 1 << n):
            sub = ""
            for i in range(n):
                if mask & (1 << i):
                    sub += s[i]
                
            if sub == sub[::-1]:
                pali[mask] = len(sub)
                
        res = 0
        for m1 in pali:
            for m2 in pali:
                if m1 & m2 == 0:
                    res = max(res, pali[m1] * pali[m2])
        
        return res