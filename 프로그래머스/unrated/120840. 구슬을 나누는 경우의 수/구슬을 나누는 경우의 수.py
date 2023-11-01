def solution(balls, share):
    answer = 1
    count = share
    for i in range(1, share+1):
        answer = answer * (balls-i+1) / i
    return answer