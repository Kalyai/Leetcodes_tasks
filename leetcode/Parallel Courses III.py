class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        bool_grafs = [0 for i in range(n)]
        grafs = [i for i in time]

        for i in range(len(relations)):
            pred, now = relations[i]
            if not(bool_grafs[now-1]):
                grafs[now-1] = time[now-1] + grafs[pred-1]
                bool_grafs[now-1] = 1
            else:
                grafs[now-1] = max(grafs[now-1], time[now-1] + grafs[pred-1])

        for i in range(len(relations)):
            pred, now = relations[i]
            if not(bool_grafs[now-1]):
                grafs[now-1] = time[now-1] + grafs[pred-1]
                bool_grafs[now-1] = 1
            else:
                grafs[now-1] = max(grafs[now-1], time[now-1] + grafs[pred-1])

        return max(grafs)


res = Solution().minimumTime(6, [[1,3],[3,2],[1,6]], [1,8,4,7,2,6])
print(res)
res = Solution().minimumTime(5, [[1,5],[2,5],[3,5],[3,4],[4,5]], [1, 2, 3, 4, 5])
print(res)
res = Solution().minimumTime(9, [[2,7],[2,6],[3,6],[4,6],[7,6],[2,1],[3,1],[4,1],[6,1],[7,1],[3,8],[5,8],[7,8],[1,9],[2,9],[6,9],[7,9]], [9,5,9,5,8,7,7,8,4])
print(res)
res = Solution().minimumTime(3, [[1, 3], [2, 3]], [3, 2, 5])
print(res)