class Solution(object):
    def groupAnagrams(self, strs):
        if len(strs) < 2:
            return [strs]

        cash = dict()
        for s in strs:
            s1 = sorted(s)
            sort_s = ''
            for j in s1:
                sort_s += j

            if sort_s in cash:
                cash[sort_s].append(s)
            else:
                cash[sort_s] = [s]

        res = list()
        for c in cash:
            res.append(cash[c])
        return res