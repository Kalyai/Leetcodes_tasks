class Solution(object):
    def longestCommonPrefix(self, l):
        if l == []:
            return ''
        mi_res = min([len(s) for s in l])
        res = ''
        for i in range(mi_res):
            x = l[0][i]
            fl = 1
            for s in l:
                if x != s[i]:
                    fl = 0
                    break
            if not(fl):
                break
            res += x
        return res
