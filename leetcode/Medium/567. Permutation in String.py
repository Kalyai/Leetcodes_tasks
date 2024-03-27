class Solution(object):
    def checkInclusion(self, s1, s2):
        count_s1 = dict()
        for string in s1:
            if string not in count_s1:
                count_s1[string] = 0
            count_s1[string] += 1

        left, right = 0, 0
        while right < len(s2):
            left = right
            if s2[right] in count_s1:
                copy_count_s2 = count_s1.copy()

                while right - left < len(s1) and right < len(s2) and s2[right] in count_s1:
                    if copy_count_s2[s2[right]] == 0:

                        while left < right and copy_count_s2[s2[right]] == 0:
                            copy_count_s2[s2[left]] += 1
                            left += 1
                    
                    copy_count_s2[s2[right]] -= 1
                    right += 1
                
                if right - left == len(s1):
                    return True
            right += 1
        return False

