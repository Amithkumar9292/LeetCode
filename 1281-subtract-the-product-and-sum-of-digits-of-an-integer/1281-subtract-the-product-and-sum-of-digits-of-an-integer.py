class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        res = 0
        res1 = 0 
        res2 = 1
        while n >0:
            r = n%10
            res1 = res1+r
            res2 = res2 *r
            n //= 10

        res = res2 -res1

        return res

            
