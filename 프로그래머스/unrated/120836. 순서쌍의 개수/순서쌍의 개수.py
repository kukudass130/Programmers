def solution(n):
    answer = 0
    a, b = 0 , 0
    answerlist = []
    while a != n:
        for i in range(1, n+1):
            if n % i ==0:
                a = i
                b = n //a
                answerlist.append((a, b))
    answer = len(answerlist)
    return answer