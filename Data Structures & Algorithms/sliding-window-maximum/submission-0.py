class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k #end is exclusive in array
        max_array = []

        while r <= len(nums):
            max_val = max(nums[l:r])
            max_array.append(max_val)
            l += 1
            r += 1
        
        return max_array