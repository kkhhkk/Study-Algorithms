# 1463번
# 정수 X에 사용할 수 있는 여산은 다음가 같이 세가지 이다.
# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면, 2로 나눈다.
# 3. 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 구하시오.
# 입력 : 첫째줄에 1보다 크거나 같고, 10^6보다 작거나 같은 정수 N이 주어진다.
# 출력 : 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

import math

n = int(input())

rst = [0]*(n+1)
for i in range(2, n+1):
    one, two, three = rst[i-1], math.inf, math.inf
    if i % 2 == 0:
        two = rst[i//2]
    if i % 3 == 0:
        three = rst[i//3]
    rst[i] = min(one, two, three) + 1

print(rst[n])
