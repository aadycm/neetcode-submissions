class Solution:
    def hammingWeight(self, n: int) -> int:
        l=[]
        while n>0:
            p = n%2
            n = n//2
            if p == 1:
                l.append(p)
        c = len(l)
        return c

        