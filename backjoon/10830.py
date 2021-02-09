# 10830번
# 크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오, 수가 매우 커질 수 있으니, A^B의 각 원소를 1000으로 나눈 나머지를 출력한다.
# 입력 : 첫째 줄에 행렬의 크기 N과 B가 주어진다, (2<=N<=5 , 1<=B<=100,000,000,000) 둘째 줄 부터 N개의 줄에 행렬의 각 원소가 주어진다. 행렬의 각 원소는
#       1000보다 작거나 같은 자연수 또는 0 이다.
# 출력 : 첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다.


def squar(A, B, n):
    arr = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for p in range(n):
                arr[i][j] += (A[i][p] * B[p][j])
            arr[i][j] %= 1000
    return arr


n, b = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

rst = [[0]*n for _ in range(n)]
for i in range(n):
    rst[i][i] = 1

while(b != 0):
    if b % 2 == 1:
        rst = squar(arr, rst, n)
    arr = squar(arr, arr, n)
    b >>= 1

for i in range(n):
    for j in range(n):
        print(rst[i][j], end=" ")
    print()
