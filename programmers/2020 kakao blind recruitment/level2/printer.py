from collections import deque

def solution(priorities, location):
    arr = [[0] for _ in range(len(priorities))]
    arr = deque(arr)
    priorities = deque(priorities)
    arr[location] = "target"
    cnt = 0
    while(len(arr)!=0):
        if priorities[0] == max(priorities):
            cnt += 1
            if arr[0] == "target":
                return cnt
            else:
                priorities.popleft()
                arr.popleft()
        else:
            priorities.append(priorities.popleft())
            arr.append(arr.popleft())