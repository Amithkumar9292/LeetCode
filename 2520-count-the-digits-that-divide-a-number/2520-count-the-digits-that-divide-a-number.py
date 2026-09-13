class Solution:
    def countDigits(self, num: int) -> int:
        temp = num
        sum1 = 0

        while temp> 0:
            r = temp%10
            if num%r== 0:
                sum1 += 1
            temp //= 10
        return sum1