def solution(places):
    answer = []
    n = len(places)
    for place in places:
        for i in range(n):
            for j in range(n):
                if place[i][j] == "P":
                    for q in range(n):
                        for p in range(n):
                            if place[q][p] == "P" and abs(i-q)+abs(j-p) <=2:
                                if q == i:
                                    if p > j:
                                        if place[i][j+1] == "X":
                                            pass
                                        else:
                                            answer.append(0)
                                            break
                                    else:
                                        if place[i][j-1] == "X":
                                            pass
                                        else:
                                            answer.append(0)
                                            break
                                elif p == j:
                                    if q >= i:
                                        if place[i+1][j] == "X":
                                            pass
                                        else:
                                            answer.append(0)
                                            break
                                    else:
                                        if place[i-1][j] == "X":
                                            pass
                                        else:
                                            answer.append(0)
                                            break
                                else:
                                    if q >= i:
                                        if place[q][p-1] == "X" and place[q-1][p] == "X":
                                            pass
                                        else:
                                            answer.append(0)
                                            break
                                    else:
                                        if place[q][p+1] == "X" and place[q+1][p] == "X":
                                            pass
                                        else:
                                            answer.append(0)
                                            break
        answer.append(1)                
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))