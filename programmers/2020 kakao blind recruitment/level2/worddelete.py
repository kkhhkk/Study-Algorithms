def solution(s):
    stack = []
    for item in s:
        if not stack:
            stack.append(item)
        elif stack[-1] == item:
            stack.pop()
        else:
            stack.append(item)
    if len(stack) == 0:
        return 1
    else:
        return 0

s = "baabaa"
print(solution(s))