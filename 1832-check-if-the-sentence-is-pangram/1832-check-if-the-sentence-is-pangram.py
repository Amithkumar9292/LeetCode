class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        ch = "abcdefghijklmnopqrstuvwxyz"

        for c in ch:
            if c not in sentence:
                return False
        return True