from itertools import permutations

def solution(expression):
    answer = 0
    x = []
    tmp = ""
    op = ["+","-","*"]
    for s in expression:
        if s.isdecimal():
            tmp += s
        else:
            x.append(tmp)
            tmp = ""
            x.append(s)
    x.append(tmp)
    
    for op_order in permutations(op,3):
        copy_x = x
        for oper in op_order:
            idx = 0
            while(idx < len(copy_x)):
                if copy_x[idx] == oper:
                    if oper == "-":
                        cal = int(copy_x[idx-1]) - int(copy_x[idx+1])
                    elif oper == "+":
                        cal = int(copy_x[idx-1]) + int(copy_x[idx+1])
                    else:
                        cal = int(copy_x[idx-1]) * int(copy_x[idx+1])
                    copy_x = copy_x[:idx-1] + [str(cal)]+ copy_x[idx+2:]
                else:
                    idx += 1
                           
        answer = max(answer, abs(int(copy_x[0])))
    return answer

expression = "100-200*300-500+20"
print(solution(expression))