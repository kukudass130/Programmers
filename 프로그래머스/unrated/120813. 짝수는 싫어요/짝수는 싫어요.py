def solution(n):
    answer = []
    array = range(1, n+1)
    for i in array:
        if i %2 != 0:
            answer.append(i)
    return answer