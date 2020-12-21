class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N ==1:
            return 1
        numOfTrust = [0 for _ in range(N+1)]
        for a, b in trust:
            numOfTrust[b] += 1
            numOfTrust[a] -= 1
        for i in range(N+1):
            if numOfTrust[i] == N -1:
                return i 
        return -1
        