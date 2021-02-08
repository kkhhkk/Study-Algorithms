# 6086번
# 농사꾼 존은 소들이 충분한 물을 마시길 원했다. 그래서 농장에서 우물에서 외양간을 잇는 N개의 배구솬의 지도를 만들기로 했다.
# 존은 아주 다양한 크기의 배수관드링 완전히 우연한 방법으로 연결돼있음을 알았다.
# 존은 파이프 통과하는 유량을 계산하고 싶다.
# 두개의 배수관이 한줄로 연결 돼 있을 때 두 관의 유량 중 최솟값으로 흐르게 된다. 예를 들어 용량이 5인 파이프가 용량이 3인 파이프와 연결되면 한개의 용량 3짜리 파이프가 된다.
# 게다가, 병렬로 연결돼 있는 배수관들은 각 용량의 합만큼 물을 보낼 수 있다.
# 마지막으로, 어떤 것에도 연결돼 ㅇㅆ지 않은 파이프는 물을 흐르게 하지 못하므로 제거된다.
# 이로 인해 복잡하게 연결된 모든 배수관들은 한개의 최대 유량을 갖는 배수관으로 만들어진다.
# 주어진 파이프들의 맵으로부터 우물(A)와 외양간 (Z) 사이의 유량을 결정하라.
# 각 노드의 이름은 알파벳으로 지어져 있다. i 번째 파이프는 두개의 다른 노드 a_i와b_i와 연결돼 있고 F_i(1<=F_i<=1,000) 만큼의 유량을 갖는다. 알파벳은 같지만, 대소문자가 다르면
# 다른 문자이다. 파이프는 양방향으로 흐를 수 있다.
# 입력 : 첫째 줄에 정수 N (1<=N<=700)이 주어진다. 둘째 줄부터 N+1 번째 줄까지 파이프의 정보가 주어진다. 첫번째, 두번째 위치에 파이프의 이름 (알파벳 대문자 또는 소문자)이 주어지고
#        세 번째 위치에 파이프의 용량이 주어진다.
# 출력 : 첫째 줄에 A에서 Z까지의 최대 유량을 출력한다.

import math

n = int(input())


def bfs(flow, capa, source, sink):
    parent = [-1]*sz
    s = [source]
    parent[source] = source
    while(len(s) != 0):
        item = s.pop(0)
        for i in range(sz):
            if parent[i] == -1 and capa[item][i] - flow[item][i] > 0:
                parent[i] = item
                s.append(i)
    return parent


def findMax(capa, source, sink):
    flow = [[0]*sz for _ in range(sz)]
    rst = 0
    while(True):
        parent = bfs(flow, capa, source, sink)
        if parent[sink] == -1:
            return rst
        q = sink
        amount = math.inf
        while(q != source):
            amount = min(amount, capa[parent[q]][q] - flow[parent[q]][q])
            q = parent[q]
        rst += amount

        q = sink
        while(q != source):
            flow[parent[q]][q] += amount
            flow[q][parent[q]] -= amount
            q = parent[q]
    return rst


sz = 128
capa = [[0]*sz for _ in range(sz)]

for _ in range(n):
    source, sink, capacity = input().split()
    s = ord(source)
    q = ord(sink)
    c = int(capacity)
    capa[s][q] += c
    capa[q][s] += c
answer = findMax(capa, ord("A"), ord("Z"))
print(answer)
