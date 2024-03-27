class Solution(object):
    def minEatingSpeed(self, piles, h):
        left, right = 1, 10 ** 9
        cnt_h = 0
        while left < right:
            mid = (left + right) // 2
            for banana in piles:
                if cnt_h > h:
                    break
                
                if banana <= mid:
                    cnt_h += 1
                
                else:
                    if banana % mid == 0:
                        cnt_h += banana // mid
                    else:
                        cnt_h += banana // mid + 1

            if cnt_h == h: 
                right = mid
                
            elif cnt_h > h: 
                left = mid + 1
                
            else: 
                right = mid
            cnt_h = 0

        return right
