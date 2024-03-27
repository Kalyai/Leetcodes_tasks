class Solution(object):
    def groupAnagrams(self, strs):
        if len(strs) <= 1:
            return [strs]

        cash = dict()
        for string in strs:
            sort_string = ''
            for i in sorted(string):
                sort_string += i

            if sort_string in cash:
                cash[sort_string].append(string)
            else:
                cash[sort_string] = [string]

        res = list()
        for elem in cash:
            res.append(cash[elem])
        return res


