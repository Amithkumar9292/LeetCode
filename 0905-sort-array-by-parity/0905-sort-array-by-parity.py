class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        arr1 =[]
        arr2 = []

        for i in range(n):
            if nums[i] %2 == 0:
                arr1.append(nums[i])
            
            if nums[i]%2 != 0:
                arr2.append(nums[i])

        return arr1+arr2


