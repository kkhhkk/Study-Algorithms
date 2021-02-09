# 17124번
# 정수 배열 A와 B가 있다. A는 총 n개의 서로 다른 양의 정수를 포함하고 B는 총 m개의 서로 다른 양의 정수를 포함한다. A,B를 이용해서 길이가 n인 새로운 배열 C를 만들어보자.
# 1 : C[i]는 배열 B에 있는 값중 A[i에 가장 가까운 값(절대값 차이가 가장 작은값)으로 정의된다.
# 2 : 만약 이 조건을 만족하는 값들이 여럿 있는 경우, 그 중 가장 크기가 작은 값으로 정의된다.
# 예를 들어, ,A=[20,5,14,9] 그리고 B=[16,8,12]라고 해보자
# C[1] = 16이다 - 왜냐하면 B[1] = 16이 A[1]=20에 가장 가깝기 땨문이다. C[2] = 8 , C[3] = 12 - 16과 12 둘다 14에 가깝지만 작은 수 이기때문, ㅊ[4] = 8이다
# 입력 : 첫 줄에 테스트 케이스의 수 t ( 1<= t <= 10) 이 주어진다. 각 테스트 케이스는 세줄에 걸쳐서 주어진다.
#       첫 출에는 N과 M이 공백으로 구분되어 주어진다. (1<= N,M <= 10^6) / 두 번째 줄에는 공백으로 구분된 N개의 정수가 주어지며, A[1]부터 A[N]을 나타낸다 (1 ~ 10^9)
#        세 번째 줄에는 공백으로 구분된 M 개의 정수가 주어지며, B[1]부터 B[M]을 나타낸다 ( 1 ~ 10^9)
# 출력 : 각 테스트 케이스에 대해 배열 C를 구하고 해당 배열의 모든  원소 합을 한줄에 출력하시오.


def findindex(one, two, three):
    index = 2
    curr = three
    if two <= curr:
        index = 1
        curr = two
    if one <= curr:
        index = 0
    return index


def binarysearch(item, B, start, end):
    diff = end - start
    if diff <= 1:
        return start
    mid = (end + start) // 2
    if item > B[mid]:
        return binarysearch(item, B, mid, end)
    else:
        return binarysearch(item, B, start, mid)


t = int(input())

rst = []
for _ in range(t):
    n, m = map(int, input().split())
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    cnt = 0
    B.sort()
    for i in range(n):
        item = A[i]
        idx = binarysearch(item, B, 0, m)
        one = abs(item - B[idx-1])
        two = abs(item - B[idx])
        three = abs(item - B[(idx+1) % m])
        index = findindex(one, two, three)
        cnt += B[idx - 1 + index]
    rst.append(cnt)

for i in range(t):
    print(rst[i])
