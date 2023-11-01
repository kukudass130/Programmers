def solution(emergency):
    answer = []
    for i in emergency:
        count = 1
        for j in range(len(emergency)):
            if i < emergency[j]:
                count = count +1
        answer.append(count)
    return answer