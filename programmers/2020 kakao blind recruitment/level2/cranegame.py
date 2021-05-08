import copy
def solution(board, moves):
    answer = 0
    board1 = copy.deepcopy(board)
    rst = []
    n = len(board)
    for item in moves:
        for x in range(n):
            if board1[x][item-1] != 0:
                if len(rst) != 0 and rst[-1] == board1[x][item-1]:
                    rst.pop()
                    answer += 2
                else:
                    rst.append(board1[x][item-1])
                board1[x][item-1] = 0
                break
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board,moves))
# 0 0 0 0 0
# 0 0 0 0 0
# 0 2 5 0 0
# 0 2 4 4 2
# 3 5 1 3 1

# 4 3 1 1 3 2 4