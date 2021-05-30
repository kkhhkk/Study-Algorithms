def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        n = len(phone_book[i])
        if n < len(phone_book[i+1]):
            if str(phone_book[i]) == str(phone_book[i+1])[:n]:
                return False
    return answer


phone_book = ["12","123","1235","567","88"]
print(solution(phone_book))


