from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque([(0,0)])
    while(len(q)!=0):
        curr_sum, num_idx = q.popleft()
        if num_idx == len(numbers):
            if curr_sum == target:
                answer += 1
        else:
            number = numbers[num_idx]
            q.append((curr_sum+number,num_idx+1))
            q.append((curr_sum-number,num_idx+1))
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))