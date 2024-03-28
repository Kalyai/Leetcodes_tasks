class Solution(object):
    def minimumTime(self, n, relations, time):
        
        grafs, grafs1 = [i for i in time], [i for i in time]
        i = 0

        for i in range(len(relations)):
            pred, now = relations[i]
            grafs[now-1] = max(grafs[now-1], time[now-1] + grafs[pred-1])

        for i in range(len(relations)-1, -1, -1):
            pred, now = relations[i]
            grafs1[now-1] = max(grafs1[now-1], time[now-1] + grafs1[pred-1])

        return max(max(grafs), max(grafs1))
        
