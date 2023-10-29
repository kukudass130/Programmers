def solution(my_string, letter):
    answer = ''
    my_list = list(my_string)
    for i in my_list:
        if i != letter:
            answer = answer+ i
    return answer