def solution(n):
    answer = 0
    nlist = list(range(n+1))
    for i in nlist:
        if i % 2 == 0:
            answer= answer + i
    return answer