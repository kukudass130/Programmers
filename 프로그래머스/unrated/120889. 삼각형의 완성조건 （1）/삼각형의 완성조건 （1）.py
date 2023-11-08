def solution(sides):
    answer = 0
    mostlong = 0
    for i in range(len(sides)):
        if mostlong < sides[i]: mostlong = sides[i]
    if sum(sides) - mostlong > mostlong:
        answer = 1
    else: answer = 2
        
    return answer