class Solution(object):
    def canFinish(self, n, l):
        def dfs(graf, visited, now):
            color[now] = 1
            visited[now] = True
            if now not in graf:
                color[now] = 2
                return

            for neighbour in graf[now]:
                if color[neighbour] == 1:
                    res.append('no')
                    break

                if not visited[neighbour]:
                    dfs(graf, visited, neighbour)
            color[now] = 2

        graf = dict()
        color = [0] * n
        visited = [0] * n
        res = list()
        for i in l:
            a, b = i[0], i[1]
            if a not in graf:
                graf[a] = []
            graf[a].append(b)

        for i in range(n):
            if not visited[i]:
                dfs(graf, visited, i)
        if res == []:
            return True
        return False
