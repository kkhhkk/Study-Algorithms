def check(position,number):
    if position == "*":
        a = 3
        b = 1
    elif position == "#":
        a = 3
        b = 3
    elif position % 3 == 0 :
        a = position // 3 - 1
        b = 3
        if position == 0:
            a = 3
            b = 2
    else:
        a = position // 3
        b = position % 3
    c = number // 3
    d = number % 3
    if number == 0:
        c = 3
        d = 2
    return abs(a-c) + abs(b-d)

def solution(numbers, hand):
    answer = ''
    left = "*"
    right = "#"
    for item in numbers:
        if item == 1 or item == 4 or item == 7:
            answer += "L"
            left = item
        elif item == 3 or item == 6 or item == 9:
            answer += "R"
            right = item
        else:
            if check(left,item) > check(right,item):
                answer += "R"
                right = item
            elif check(left,item) < check(right,item):
                answer += "L"
                left = item
            else:
                if hand == "right":
                    answer += "R"
                    right = item
                else:
                    answer += "L"
                    left = item
    return answer


numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
print(solution(numbers,hand))