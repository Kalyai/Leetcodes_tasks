class Solution(object):
    def sortColors(self, nums):

        red, white, blue = 0, 0, len(nums) - 1
        i = 0
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[blue], nums[white] = nums[white], nums[blue]
                blue -= 1
