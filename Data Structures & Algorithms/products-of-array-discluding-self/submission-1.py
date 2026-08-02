class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = [1] * len(nums)
        left = [1] * len(nums)
        product = 1
        res = []

        for i in range(len(nums) - 1, -1, -1):
            right[i] = product
            product *= nums[i]

        product = 1
        for i in range(len(nums)):
            left[i] = product
            product *= nums[i]
        for i in range(len(nums)):
            res.append( right[i] * left[i] )
        return res
        