def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0 and i not in answer:
            answer.append(i)
    return answer