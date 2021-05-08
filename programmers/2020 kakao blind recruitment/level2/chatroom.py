def solution(record):
    answer = []
    userid = {}
    for item in record:
        info = item.split()
        if info[0] == "Enter" or info[0] == "Change":
            userid[info[1]] = info[2]

    for item in record:
        info = item.split()
        if info[0] == "Enter":
            answer.append(f"{userid[info[1]]}님이 들어왔습니다.")
        elif info[0] == "Leave":
            answer.append(f"{userid[info[1]]}님이 나갔습니다.")
        
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))