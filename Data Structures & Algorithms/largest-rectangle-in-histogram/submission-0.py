class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                prev_start, prev_height = stack.pop()

                width = i - prev_start
                area = prev_height * width
                max_area = max(max_area, area)

                start = prev_start
        
            stack.append((start, h))


        n = len(heights)
        for start, height in stack: 
            area = height * (n - start)
            max_area = max(area, max_area)
        
        return max_area

