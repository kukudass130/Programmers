def solution(my_string):
    answer = ''
    xarray = ['a', 'e', 'i', 'o', 'u']
    for i in my_string:
        if i not in xarray:
            answer = answer + i
    return answer