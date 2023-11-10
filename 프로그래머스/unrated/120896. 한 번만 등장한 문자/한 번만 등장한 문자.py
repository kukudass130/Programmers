def solution(s):
    answer = ''
    chrdict = {}
    for i in s:
        if i in chrdict:
            chrdict[i] = chrdict[i] + 1
        else:
            chrdict[i] = 1
    for k, v in chrdict.items():
        if v == 1:
            answer += k
    return ''.join(sorted(answer))