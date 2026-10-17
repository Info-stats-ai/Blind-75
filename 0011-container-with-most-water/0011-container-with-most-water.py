class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxA = 0

        l = 0
        r = len(height) - 1
        while l < r:
            area = min(height[l], height[r])*(r-l)
            maxA = max(area, maxA)
            if height[l] < height[r]:
                l += 1
            else:
                r -=1
        return maxA


        