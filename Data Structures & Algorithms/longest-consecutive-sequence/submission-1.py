class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)

        best_length = 0

        for num in nums:
            curr_length = 0

            if num - 1 not in unique_nums:
                curr_length = 1
                start = num
                while start + 1 in unique_nums:
                    start = start + 1
                    curr_length += 1
                best_length = max(best_length, curr_length)
            else:
                pass
        
        return best_length

        