class Solution(object):
    def mergeKLists(self, lists):

        i = 0
        max_len = max([len(i) for i in lists])
        res = list()
        fl = 0
        while i != max_len:
            x = list()
            pred = 0
            cnt = 0
            for j in lists:
                if len(j) > i:
                    print(j[i])
                    if len(x) == 0:
                        pred = j[i]
                        x.append(j[i])
                        cnt += 1
                    else:
                        if j[i] >= pred:
                            x.append(j[i])
                            pred = j[i]
                            cnt += 1
                        else:
                            for j1 in range(cnt):
                                if x[j1] > j[i]:
                                    fl = 1
                                else:
                                    x = x[:j1] + [j[i]]
                                    fl = 0
                                    break
                            if fl:
                                x = [j[i]] + x
            res += x
            i += 1
        return res

res = Solution().mergeKLists([[1, 4, 5], [1, 3, 4], [2, 6]])
print(res)