class Solution(object):
    def isAnagram(self, s, t):
        cnt1, cnt2 = dict(), dict()
        for s1 in s:
            if s1 not in cnt1:
                cnt1[s1] = 0
            cnt1[s1] += 1

        for t1 in t:
            if t1 not in cnt2:
                cnt2[t1] = 0
            cnt2[t1] += 1

        for c1 in cnt1:
            if c1 not in cnt2:
                return False
            if cnt2[c1] != cnt1[c1]:
                return False

        if len(cnt1) < len(cnt2):
            return False
        return True
