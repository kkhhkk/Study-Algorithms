import math
from collections import deque

def solution(n, start, end, roads, traps):
    times = [[0]*(n) for _ in range(n)]
    x = []
    for line in roads:
        times[int(line[0]-1)][int(line[1]-1)] += int(line[2])
    for trap in traps:
        x.append(int(trap))

    print(times)
    parent = [0]*n
    s = deque([start-1])
    parent[start-1] = 0
    proceed = True
    while(proceed):
        print(s)
        item = s.popleft()
        for i in range(n):
            if times[item][i] != 0:
                s.append(i)
                parent[i] = parent[item] + times[item][i]
                if i+1 in x:
                    for j in range(n): 
                        tmp = times[i][j]
                        tmp1 = times[j][i]
                        times[j][i] = tmp
                        times[i][j] = tmp1
                if i == end-1:
                    proceed = False
        
    return parent[end-1]

n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2,3]
print(solution(n,start,end,roads,traps))