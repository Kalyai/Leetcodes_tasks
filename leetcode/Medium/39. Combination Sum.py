class Solution(object):
    def combinationSum(self, candidates, target):
        def backtracking(start, target, res_candidates):
            if target == 0:
                result.append(res_candidates)
            elif target < 0:
                return
            else:
                for i in range(start, len(candidates)):
                    backtracking(i, target - candidates[i], res_candidates + [candidates[i]])

        result = list()
        backtracking(0, target, [])
        return result
