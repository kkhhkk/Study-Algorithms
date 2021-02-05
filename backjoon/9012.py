# 9012번
# 괄호 문자열은 두개의 괄호 기호인 "(" 와 ")"만으로 구성돠어 있는 문자열이다. 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열일고 부른다.
# 한쌍의 괄호 기호로 된 "()" 문자열은 기본 VPS이라고 부른다, 만일 x가 VPS라면 이것을 하나의 괄호에 넣은 새로운 문자열 "(X)"도 VPS가 된다. 그리고 두 VPS
# y를 접합시킨 새로운 무자열 xy도 VPS가 된다. 예를들어, "(())()" 와 "((()))"는 VPS이지만, "(()(","())()))" 그리고 "(()"는 모두 VPS가 아닌 문자열이다.
# 여러분은 입력으로 주어진 괄호 문자열이 VPS인지 아닌지를 판단해서 그 결과를 YES와 NO로 나타내어야한다.

# 입력 : 입력데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다. 입력의 첫 번째 줄에는 입력 데이터 수를 나타내는 정수 T가 주어진다.
#        각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다 하나의 괄호 문자열의 길니는 2이상 50이하이다.
# 출력 : 출력은 표준 출력을 사용한다.만일 입력 괄호 문자열이 올바른 과로 문자열이면 "YES" 아니면 "NO" 를 한 줄에 하나씩 차례대로 출력

t = int(input())

arr = []
for _ in range(t):
    arr.append(list(map(str, input())))


result = []
for line in arr:
    rst = []
    for item in line:
        if item == "(":
            rst.append(item)
        else:
            if len(rst) == 0:
                rst.append(1)
                break
            else:
                rst.pop()
    if len(rst) == 0:
        result.append("YES")
    else:
        result.append("NO")

for i in range(t):
    print(result[i])


2


def solve():
    arr = input()
    rst = []
    for item in arr:
        if item == "(":
            rst.append(item)
        else:
            if len(rst) == 0:
                return print("NO")
            else:
                rst.pop()

    if len(rst) == 0:
        return print("YES")
    else:
        return print("NO")


t = int(input())
for _ in range(t):
    solve()
