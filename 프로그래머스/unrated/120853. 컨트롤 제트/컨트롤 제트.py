def solution(s):
    answer = 0
    numlist = list(s.split(" "))
    for i in range(len(numlist)):
        if numlist[i] == "Z":
            answer = answer - int(numlist[i -1])
        else:
            answer = answer + int(numlist[i])
    return answer