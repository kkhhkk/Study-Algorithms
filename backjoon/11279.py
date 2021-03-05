# 11279
# 문제
# 널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

# 배열에 자연수 x를 넣는다.
# 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

# 입력
# 첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다.
# 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우이다.
# 입력되는 자연수는 231보다 작다.

# 출력
# 입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 된다.

# 1
import heapq
import sys

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print("0")
    else:
        heapq.heappush(heap, [-num, num])

# 2


def insert(heap, num):
    heap.append(num)
    i = len(heap) - 1
    while(i > 1):
        if heap[i//2] < heap[i]:
            heap[i//2], heap[i] = heap[i], heap[i//2]
            i = i//2
        else:
            break


def remove(heap):
    heap[1], heap[-1] = heap[-1], heap[1]
    maxVal = heap.pop()
    i = 1
    check = i
    left = 2*i
    right = 2*i+1
    while(i <= len(heap)//2):
        if left < len(heap) and heap[check] < heap[left]:
            check = left
        if right < len(heap) and heap[check] < heap[right]:
            check = right
        if check != i:
            heap[i], heap[check] = heap[check], heap[i]
            i = check
        else:
            break
    return maxVal


n = int(sys.stdin.readline())
heap = [0]

for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) == 1:
            print("0")
        else:
            print(remove(heap))
    else:
        insert(heap, num)
