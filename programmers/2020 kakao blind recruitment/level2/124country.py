def solution(n):
    cnt = 0
    i = 1
    while(n != 0):
        a = n
        b = 10**(i-1)
        if a % 3 == 0:
            cnt += b*4
            n = a//3 - 1
        else:
            cnt += b*(a % 3)
            n = a // 3
        i += 1
    return str(cnt)