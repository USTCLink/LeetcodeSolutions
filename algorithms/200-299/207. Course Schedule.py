class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for prev, current in prerequisites:
            graph[prev].append(current)
        visited = set()
        ancestors = set()
        
        def isCyclicRecur(idx):
            visited.add(idx)
            ancestors.add(idx)
            
            for v in graph[idx]:
                if v not in visited:
                    if isCyclicRecur(v):
                        return True
                elif v in ancestors:
                    return True
                
            ancestors.remove(idx)
            return False
        
        for i in range(len(graph)):
            if i not in visited:
                if isCyclicRecur(i):
                    return False
        return True
        
        