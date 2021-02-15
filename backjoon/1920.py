# 1920번
# 문제
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100, 000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100, 000)이 주어진다.
# 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 - 231 보다 크거나 같고 231보다 작다.

# 출력
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

n = int(input())
A = [int(x) for x in input().split()]
m = int(input())
B = [int(x) for x in input().split()]

A.sort()


def findB(A, item, start, end):
    diff = end - start
    if diff <= 1 and A[start] != item:
        return False
    mid = (start + end) // 2
    if A[mid] == item:
        return True
    if A[mid] > item:
        return findB(A, item, start, mid)
    if A[mid] < item:
        return findB(A, item, mid, end)


for item in B:
    if findB(A, item, 0, n):
        print(1)
    else:
        print(0)
