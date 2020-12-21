class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False for _ in range(n)]
        graph = [[] for _ in range(n)]
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
            
        def dfs(i):
            if visited[i]:
                return 
            visited[i] = True
            neighbors = graph[i]
            for _next in neighbors:
                dfs(_next)
        
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)
        return count