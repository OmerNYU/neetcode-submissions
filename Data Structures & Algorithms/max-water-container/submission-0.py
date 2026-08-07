class Solution:
    def maxArea(self, heights: List[int]) -> int:

        resArea = 0
        right = len(heights) - 1
        left = 0
        

        while left < right:
            curr_area = min(heights[left], heights[right]) * (right - left)

            if heights[left] < heights[right]:
                left += 1
            
            else:
                right -= 1
            

            resArea = max(resArea, curr_area)
        return resArea

            