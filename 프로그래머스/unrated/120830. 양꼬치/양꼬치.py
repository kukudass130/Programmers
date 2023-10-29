def solution(n, k):
    answer = 0
    bonus = 0
    if n >= 10:
        bonus = n // 10
        k = k - bonus
    answer = n * 12000 + k * 2000
    return answer