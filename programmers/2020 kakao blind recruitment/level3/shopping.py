import math
answer = math.inf

def solution(gems):
    n = len(set(gems))
    dic = {gems[0]:1}
    tmp = [0, len(gems)-1]
    start, end = 0,0

    while(start < len(gems) and end < len(gems)):
        if len(dic) == n:
            if end - start < tmp[1] - tmp[0]:
                tmp = [start, end]
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == len(gems):
                break
            if dic.get(gems[end]) is None:
                dic[gems[end]] = 1
            else:
                dic[gems[end]] += 1
        
    tmp[0] += 1
    tmp[1] += 1
    return tmp

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))
print(answer)