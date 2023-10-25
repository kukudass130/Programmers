def solution(array):
    answer = 0
    num = {}
    for i in array:
        if i in num:
            num[i] = num[i] + 1
        else:
            num[i] = 1
    count = 0
    for j in list(num.keys()):
        if num[j] == count:
            answer = -1
        elif num[j] > count:
            count = num[j]
            answer = j
    return answer