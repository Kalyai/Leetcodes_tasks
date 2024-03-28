class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        if n > m:
            nums1, nums2 = nums2, nums1
            n, m = m, n

        all_len = (n + m)
        half_len = (all_len + 1) // 2

        left, right = 0, n
        while left <= right:
            position1 = (left + right) // 2
            position2 = half_len - position1

            min1 = float('-inf') if position1 == 0 else nums1[position1 - 1]
            max1 = float('inf') if position1 == n else nums1[position1]

            min2 = float('-inf') if position2 == 0 else nums2[position2 - 1]
            max2 = float('inf') if position2 == m else nums2[position2]

            if min1 <= max2 and min2 <= max1:
                if all_len % 2 != 0:
                    return max(min1, min2)
                else:
                    res = float(max(min1, min2) + min(max1, max2))
                    res /= 2
                    return res

            if min1 > max2:
                right = position1 - 1
            else:
                left = position1 + 1
