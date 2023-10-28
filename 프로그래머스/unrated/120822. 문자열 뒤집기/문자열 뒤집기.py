def solution(my_string):
    answer = ''
    my_list = list(my_string)
    for i in range(len(my_list)):
        answer = answer + my_list[len(my_list)-(i+1) ]
    return answer