def solution(array):
    answer = []
    tmp = [0, 0]
    for k, v in enumerate(array):
        if v > tmp[0]:
            tmp[0] = v
            tmp[1] = k
    answer = tmp
    return answer