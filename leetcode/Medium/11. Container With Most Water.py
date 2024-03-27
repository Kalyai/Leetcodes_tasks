class Solution:
    def maxArea(self, height):
        res = 0
        left, right = 0, len(height) - 1
        while left < right:
            cur = min(height[left], height[right]) * (right - left)
            res = max(res, cur)
          
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
            
        return res
