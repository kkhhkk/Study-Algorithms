# from itertools import combinations

# def solution(orders, course):
#     answer = []
#     union = []
#     rst = 0
#     count = 0
#     list_pivot = []
#     for order in orders:
#         for item in order:
#             if item not in union:
#                 union.append(item)
#     union.sort()
#     for num in course:
#         for item in combinations(union, num):
#             cnt = 0
#             pivot = ""
#             for s in item:
#                 pivot += s
#             for order in orders:
#                 if len(pivot) <= len(order):
#                     for item in pivot:
#                         if item in order:
#                             count += 1
#                     if count == len(pivot):
#                         cnt += 1
#                     count = 0
#             rst = max(rst,cnt)        
#             list_pivot.append((cnt,pivot))
#         for lst in list_pivot:
#             if lst[0] >= 2 and lst[0] == rst:
#                 answer.append(lst[1])
#         list_pivot = []
#         rst = 0
#     answer.sort()
#     return answer


# from itertools import combinations

# def solution(orders, course):
#     answer = []
#     for num in course:
#         set_menu = {}
#         temp = []
#         for order in orders:
#             temp += combinations(sorted(order), num)
#         for tmp in temp:
#             key = "".join(tmp)
#             if key in set_menu:
#                 set_menu[key] += 1
#             else:
#                 set_menu[key] = 1
#         print(set_menu)
#         for menu in set_menu:
#             if max(set_menu.values()) > 1:
#                 if set_menu[menu] == max(set_menu.values()):
#                     answer.append(menu)
#     answer.sort()
#     return answer

from collections import Counter
from itertools import combinations  

def solution(orders, course):
    answer = []
    for num in course:
        temp = []
        for order in orders:
            temp += combinations(sorted(order), num)
        counter = Counter(temp)
        print(counter)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += ["".join(x) for x in counter if counter[x] == max(counter.values())]
    answer.sort()
    return answer

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]	
solution(orders, course)