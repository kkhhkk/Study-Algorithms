def gcd(w,h):
    if w < h :
        (w,h) = (h,w)
    while(h!=0):
        (w,h) = (h,w%h)
    return w

def solution(w,h):
    return w*h - w - h + gcd(w,h)

w = 8
h = 12
print(solution(w,h))