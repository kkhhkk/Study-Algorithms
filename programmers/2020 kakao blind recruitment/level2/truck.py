from collections import deque

def solution(bridge_length, weight, truck_weights):
    n = len(truck_weights)
    q = deque(truck_weights)
    cnt = 0
    ing = deque([])
    rst = []
    time = deque([])
    while(len(rst)<n):
        cnt += 1
        if time and cnt == time[0] + bridge_length:
            rst.append(ing.popleft())
            time.popleft()
        if q and q[0] + sum(ing) <= weight:
            ing.append(q.popleft())
            time.append(cnt)
        
    return print(cnt)

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
solution(bridge_length, weight, truck_weights)

