def solution(n):
    answer = 0
    i = 0
    while i**2 <= n and answer != 1:
        if i **2 == n:
            answer = 1
        else:
            i += 1
            answer = 2
    return answer