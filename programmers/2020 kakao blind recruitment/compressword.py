# 문자열 압축
# 데이터 처리 전문가가 되고 싶은 "어피치"는 문자열을 압축하는 방법에 대해 공부를 하고있습니다. 최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고있는데,
# 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현한ㄴ 알고리즘을 공부하고 있습니다.
# 예로, "aabbaccc"의 경우 "2a2ba3c" (문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데, 이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다.
# 예를들어, "abcabcdede"와 같은 묹열은 전혀 압축되지 않습ㄴ니다. "어피치"는이러한 단점을 해결하기 위해 문자열을 1개 이상의 단이ㅜ로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을
# 찾아보려고 합니다. 예를들어, "ababcdcdababcdcd"의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축한다면 "2ab2cd2ab2cd"로 표현할 수 있다. 다른방법으로는 8개 단위
# 로 잘라서 압축한다면 "2ababcdcd"로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다. 다른예로, ,"abcabcdede"와 같은경우, 문자를 2개 단위로 잘라서 압축하몀ㄴ "abcabc2de"
# 가 되지만 , 3개씩 자르면 "2abcdede"가 되어 가장 짧은 압축방법이 됩니다. 이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.
# 압축할 문자열 s가 매겨변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 retrun 하도록 solution 함수를 완성해주세요.
# 제한사항 : s의 길이는 1이상 1000이하이다. / s는 소문자로만 이루어져있다.

import math


def compress(s, cut):
    pivot = s[:cut]
    rst = len(pivot)
    cnt = 1
    for i in range(cut, len(s), cut):
        if pivot == s[i:i+cut]:
            cnt += 1
        else:
            if cnt != 1:
                rst += len(str(cnt))
                cnt = 1
            pivot = s[i:i+cut]
            rst += len(pivot)
    if cnt != 1:
        rst += len(str(cnt))
    return rst


def solution(s):
    answer = math.inf
    if len(s) <= 2:
        return len(s)
    else:
        for i in range(1, len(s)//2+1):
            answer = min(answer, compress(s, i))

    return answer


s = input()
print(solution(s))
