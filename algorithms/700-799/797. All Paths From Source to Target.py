class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        def dfs(i, path):
            if i == n - 1:
                res.append(path)
            for _next in graph[i]:
                dfs(_next, path + [_next])
        dfs(0, [0])
        return res
                