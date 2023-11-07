def solution(n):
    answer = []  
    for i in range(2, n+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count = count +1
        if count == 2:
            if n % i == 0:
                answer.append(i)
    return answer