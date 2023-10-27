def solution(num_list):
    answer = []
    length = len(num_list)
    for i in list(range(0, length)):
        answer.append(num_list[length-1-i])
    return answer