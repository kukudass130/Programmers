def solution(slice, n):
    answer = 0
    while slice * answer < n:
        answer = answer + 1
    return answer