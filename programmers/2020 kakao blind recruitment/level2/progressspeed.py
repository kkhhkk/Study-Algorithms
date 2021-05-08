def solution(progresses, speeds):
    answer = []
    rst = []
    n = len(speeds)
    for i in range(n):
        want = 100 - progresses[i]
        if want % speeds[i] == 0:
            rst.append(want//speeds[i])
        else:
            rst.append(want//speeds[i]+1)
    pivot = rst[0]
    cnt = 0
    i = 0
    while(i != len(rst)):
        if pivot >= rst[i]:
            cnt += 1
        else:
            answer.append(cnt)
            pivot = rst[i]
            cnt = 0
            i -= 1
        i+= 1
    if cnt != 0:
        answer.append(cnt)
    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses,speeds))