def solution(num_list, n):
    answer = []
    length = len(num_list)
    subarray = []
    for i in range(length):
        subarray.append(num_list[i])
        if len(subarray) == n:
                answer.append(subarray) 
                subarray = []
    return answer