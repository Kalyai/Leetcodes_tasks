class Solution(object):
    def trap(self, height):
        max_elem = -1
        index_max = 0
        for i in range(len(height)):
            if height[i] > max_elem:
                max_elem = height[i]
                index_max = i

        left, right = 0, 1
        summ = 0
        while right < index_max:
            if height[left] > height[right]:
                summ += height[left] - height[right]
                right += 1
                
            else:
                left = right
                right += 1

        left, right = len(height) - 1, len(height) - 2
        while right > index_max:
            if height[left] > height[right]:
                summ += height[left] - height[right]
                right -= 1
                
            else:
                left = right
                right -= 1
        return summ
