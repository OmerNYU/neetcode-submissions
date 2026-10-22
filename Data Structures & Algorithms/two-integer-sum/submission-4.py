class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        
        for idx, num in enumerate(nums):
            needed = target - num

            if needed in seen:
                return [seen[needed], idx]

            else:
                seen[num] = idx

                