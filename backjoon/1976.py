# 1976번
# 동현이는 친구들과 함께 여행을 가려고 한다. 한국에는 도시가 N개 있고 임의의 두 도시 사이에 길이 있을 수도, 없을 수도 있다. 동현이의 여행 일정이 주어졌을 때, 이 여행 경로가 가능한 것인지 알아보자.
# 물론 중간에 다른 도시를 경유해서 여행을 할 수도 있다. 예를 들어 도시가 5개 있고, A-B,B-C,A-D,B-D,E-A의 길이 있고, ,동혁이의 여행 계획이 E C B C D 라면 E-A-B-C-B-C-B-D라는 여행결오를 통해 목적
# 을 달성할 수 있다. 도시들의 개수와 도시들 간의 연결여부가 주어져 있고, 동혁이의 여행 계획에 속한 도시들이 순서대로 주어 졌을 때 (중복가능) 가능한지 여부를판별하는 프로그램을 작성하시오.
# 입력 : 첫 줄에 도시의 수 n이 주어진다. n은 200 이하다. 둘째 줄에 여행 계획에 속한 도시들의 수 M이 주어진다. M은 1000이하이다. 다음 N*N 행렬을 통해 임의의 두 도시가 연결되었는지에 관한
#        정보가 주어진다. 1이면 연결된 것이고 0이면 연결이 되지 않은 것이다. A와 B가 연결되어있으면 B와 A도 연결되어 있다. 마지막 줄에는 여행 계획이 주어진다.
# 출력 : 첫 줄에 가능하면 YES 불가능하면 NO를 출력한다


n = int(input())
m = int(input())

bridge = []
for _ in range(n):
    bridge.append(list(map(int, input().split())))

plan = [int(x)-1 for x in input().split()]

parent = [int(x) for x in range(n)]


def get_parent(parent, x):
    if parent[x] == x:
        return x
    else:
        parent[x] = get_parent(parent, parent[x])
        return parent[x]


def findparent(parent, i, j):
    i = get_parent(parent, i)
    j = get_parent(parent, j)
    if i <= j:
        parent[j] = i
    else:
        parent[i] = j


for i in range(n):
    for j in range(i, n):
        if bridge[i][j] == 1:
            findparent(parent, i, j)

pivot = get_parent(parent, plan[0])
cnt = 0
for item in plan:
    if pivot == get_parent(parent, item):
        cnt += 1

if cnt == m:
    print("YES")
else:
    print("NO")
