class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        small = min(nums)
        large = max(nums)
        result = []

        for i in range (small, large+1):
            if i not in nums:
                result.append(i)
        return result

            