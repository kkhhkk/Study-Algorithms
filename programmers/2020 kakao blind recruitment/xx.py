def check_type(rules, com, answer):
    num = "0123456789"
    for j in range(1, len(com)):
        for key in rules.keys():
            c_key = key[1:]
            if c_key in com[j]:
                arg = str(rules[key])
                com[j] = com[j][len(key):]
                rst = 0
                for s in com[j]:
                    if s in num:
                        rst += 1
                if rst == 0:
                    com[j] == ""
                elif rst == len(com[j])-1:
                    com[j] = int(com[j])
                else:
                    com[j] = str(com[j])
                print(arg, type(com[j]))
                if arg == "STRING":
                    if type(com[j]) != str:
                        return answer.append(False)
                if arg == "NUMBER":
                    if type(com[j]) != int:
                        return answer.append(False)
                if arg == "NULL":
                    if com[j] == "":
                        pass
                    else:
                        return answer.append(False)
    return answer.append(True)


def solution(program, flag_rules, commands):
    answer = []

    if len(program) < 1 or len(program) > 10:
        return False
    if len(flag_rules) < 1 or len(flag_rules) > 100:
        return False
    # flag_rules를 name arg 에 맞게 저장
    rules = {}
    for q in range(len(flag_rules)):
        name, arg = flag_rules[q].split()
        if 2 <= len(name) <= 10:
            if arg == "NULL" or arg == "NUMBER" or arg == "STRING":
                rules[name] = arg
    if len(commands) > 100:
        return False
    for command in commands:
        if command[:len(program)] != program:
            answer.append(False)
            break
        # command 를 -(dash) 로 구분
        com = command[len(program):].split("-")
        check_type(rules, com, answer)

    return print(answer)


program = "line"
flag_rules = ["-s STRING", "-n NUMBER", "-e NULL"]
commands = ["line -n 100 -s hi -e", "lien -s Bye"]
solution(program, flag_rules, commands)
