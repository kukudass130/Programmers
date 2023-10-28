def solution(my_string, n):
    answer = ''
    string_list = list(my_string)
    for i in string_list:
        answer = answer + i * n
    return answer