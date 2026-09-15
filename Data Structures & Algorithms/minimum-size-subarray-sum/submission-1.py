class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0

        shortest = 100001
        total = 0


        for r in range(len(nums)):
            total += nums[r]
            
            
            while total >= target:
                shortest = min(shortest, r - l + 1)
                total -= nums[l]
                l += 1
        
        if shortest == 100001:
            return 0
        else:
            return shortest


        


