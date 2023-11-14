def solution(quiz):
    answer = []
    for i in quiz:
        ilist = i.split(" ")
        s = " ".join(ilist[:3])
        if eval(s) == int(ilist[4]):
            answer.append("O")
        else:
            answer.append("X")
    return answer