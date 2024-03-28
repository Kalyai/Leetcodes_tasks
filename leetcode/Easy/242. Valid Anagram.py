class Solution(object):
    def isAnagram(self, s, t):
        cnt1, cnt2 = dict(), dict()
        for string1 in s:
            if string1 not in cnt1:
                cnt1[string1] = 0
            cnt1[string1] += 1

        for string2 in t:
            if string2 not in cnt2:
                cnt2[string2] = 0
            cnt2[string2] += 1

        for c1 in cnt1:
            if c1 not in cnt2:
                return False
            if cnt2[c1] != cnt1[c1]:
                return False

        if len(cnt1) < len(cnt2):
            return False
        return True
