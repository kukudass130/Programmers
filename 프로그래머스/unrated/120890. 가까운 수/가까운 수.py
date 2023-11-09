def solution(array, n):
    answer = 0
    maindiffer = None
    for i in array:
        differ = i - n
        if differ < 0:
            differ = differ * (-1)
        if maindiffer == None or maindiffer == differ:
            if answer > i:
                answer = i
        if maindiffer == None or differ < maindiffer:
            maindiffer = differ
            answer = i
    return answer