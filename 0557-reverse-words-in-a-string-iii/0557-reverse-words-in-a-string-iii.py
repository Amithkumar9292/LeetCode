class Solution:
    def reverseWords(self, s: str) -> str:

        word = s.split()
        res1 = []
        result =" "

        for i in word:
            res = " "
            res = i[::-1]
            res1.append(res)
        result = " ".join(res1)
        return result
