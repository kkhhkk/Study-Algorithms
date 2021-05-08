def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key=len)
    for lst in s:
        li = lst.split(",")
        for j in li:
            if int(j) not in answer:
                answer.append(int(j))
    return answer

    

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))