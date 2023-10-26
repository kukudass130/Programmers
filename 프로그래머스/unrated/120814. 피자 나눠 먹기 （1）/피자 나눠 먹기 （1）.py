def solution(n):
    answer = 0
    count = n
    while count > 7 :
        answer = answer +1
        count = count- 7
    answer = answer + 1
    return answer