def solution(n):
    answer = 0
    total = 1
    while total <= n:
        answer = answer +1
        total = total * answer
    answer = answer - 1
    return answer