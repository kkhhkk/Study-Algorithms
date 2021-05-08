from itertools import permutations

def solution(user_id, banned_id):
    answer = []
    for user_list in permutations(user_id,len(banned_id)):
        cnt = 1
        for i in range(len(banned_id)):
            if len(user_list[i]) != len(banned_id[i]):
                cnt = 0
                break
            else:
                for j in range(len(user_list[i])):
                    if banned_id[i][j] == "*":
                        pass
                    elif user_list[i][j] != banned_id[i][j]:
                        cnt = 0
                        break
        if cnt == 1:
            user_list = set(user_list)
            if user_list not in answer:
                answer.append(user_list)
    return len(answer)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
print(solution(user_id, banned_id))