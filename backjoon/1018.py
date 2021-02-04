# 1018번

# M x N 보드. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져있다.
# 이보드를 잘라서 8 x 8 크리의 체스판으로 만드려고 한다.

# 입력 : 첫째줄에는 N과 M이 주어진다.  8<= N,M <= 50 둘째줄은 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며 W 흰색이다.
# 출력 : 첫째 줄에 지민이가 다시 칠해 하는 정사각형 개수의 최솟값을 출력한다.

n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(str, input())))

str1 = "BWBWBWBW"
str2 = "WBWBWBWB"
pivot1 = [str1, str2, str1, str2, str1, str2, str1, str2]
pivot2 = [str2, str1, str2, str1, str2, str1, str2, str1]

rst = 65
for i in range(n-7):
    for j in range(m-7):
        cnt = 0
        for p in range(i, i+8):
            for q in range(j, j+8):
                if board[p][q] != pivot1[p-i][q-j]:
                    cnt += 1
        rst = min(rst, cnt)
        cnt = 0
        for p in range(i, i+8):
            for q in range(j, j+8):
                if board[p][q] != pivot2[p-i][q-j]:
                    cnt += 1
        rst = min(rst, cnt)

print(rst)
