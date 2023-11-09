def solution(order):
    answer = 0
    numlist =[]
    while order != 0:
        numlist.append(order %10)
        order = order // 10
    for i in numlist:
        if i in [3, 6, 9]:
            answer = answer +1
    return answer