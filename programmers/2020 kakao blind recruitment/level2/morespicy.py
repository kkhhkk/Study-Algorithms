import heapq

def solution(scoville, K):
    answer = 0
    h = []
    for item in scoville:
        heapq.heappush(h,item)
    while(h[0] < K):
        answer += 1
        try:
            heapq.heappush(h,heapq.heappop(h)+heapq.heappop(h)*2)
        except:
            return -1
    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville,K))