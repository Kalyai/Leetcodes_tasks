class Solution(object):
    def findSubstring(self, s, words):
        if len(s) == 1 and len(words) == 1:
            if s in words:
                return [0]
            else:
                return []
        n = len(s)
        h1 = dict()
        h2 = dict()
        for i in words:
            h2[i] = 0
            if i not in h1:
                h1[i] = 1
            else:
                h1[i] += 1
        
        len_st = len(words[0])
        i = 0
        res = list()
        l_words = len(words)
        
        while i < n:
            j = i + len_st
            s1 = s[i:j]
            h3 = h2.copy()
            cnt = 0
            while s1 in h1 and j < n and cnt < l_words:
                h3[s1] += 1
                s1 = s[j+(len_st * cnt):j+ len_st * (cnt + 1)]
                cnt += 1
            if h3 == h1:
                res.append(i)
            i += 1
        return res
