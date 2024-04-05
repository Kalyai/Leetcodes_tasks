class Solution(object):
    def combinationSum2(self, candidates, target):
        def main(candidates, summ, list_of_sums, target):
            if summ == target:
                result.append(list_of_sums)
                return list_of_sums
            elif summ < target:
                i = 0
                while i < len(candidates):
                    main(candidates[i + 1:], summ + candidates[i], list_of_sums + [candidates[i]], target)
                    while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                        i += 1
                    i += 1
            else:
                return

        candidates.sort()
        result = list()
        used = set()
        for i in range(len(candidates)):
            if candidates[i] in used:
                continue
            main(candidates[i + 1:], candidates[i], [candidates[i]], target)
            used.add(candidates[i])
        return result
