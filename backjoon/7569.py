# 7576번 3차원 문제
import sys
from collections import deque
input = sys.stdin.readline

n, m, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(m)] for _ in range(h)]
q = deque()
rst = 0
for i in range(h):
    for j in range(m):
        for k in range(n):
            rst += arr[i][j][k]
            if arr[i][j][k] == 1:
                q.append((i, j, k))


dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    while(q):
        z, x, y = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nz < h and 0 <= nx < m and 0 <= ny < n:
                if arr[nz][nx][ny] == 0:
                    q.append((nz, nx, ny))
                    arr[nz][nx][ny] = arr[z][x][y] + 1


def solve():
    if rst == n*m*h:
        return print(0)
    bfs()
    result = -2
    for i in range(h):
        for j in range(m):
            for k in range(n):
                if arr[i][j][k] == 0:
                    return print(-1)
                result = max(result, arr[i][j][k])
    return print(result-1)


solve()
