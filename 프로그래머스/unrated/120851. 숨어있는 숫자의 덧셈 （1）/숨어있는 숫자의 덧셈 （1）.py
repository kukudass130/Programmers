def solution(my_string):
    answer = 0
    numlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in my_string:
        if i in numlist:
            answer = answer + int(i)
    return answer