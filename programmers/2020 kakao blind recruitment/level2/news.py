def solution(str1, str2):
    list_str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    list_str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

    union = list_str1
    intersection = []
    for item in list_str1:
        if item in list_str2:
            intersection.append(item)
            list_str2.remove(item)
    if list_str2:
        for item in list_str2:
            union.append(item)
    if len(list_str1) == 0 and len(list_str2) == 0:
        answer = 65536
    else:
        answer = int(len(intersection)/len(union)*65536)
    return answer
str1 = "handshake"
str2 = "shake hands"
print(solution(str1,str2))