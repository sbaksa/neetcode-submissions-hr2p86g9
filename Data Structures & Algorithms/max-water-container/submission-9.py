class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0, len(heights)-1
        maxh = 0
        while l < r:
            width = r - l
            length = min(heights[l],heights[r])

            area = length * width

            maxh = max(area, maxh)

            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1

        return maxh