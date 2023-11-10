def solution(my_string, num1, num2):
    answer = ''
    str1, str2, str3 ='','',''
    if num1 < num2:
        str1 = my_string[:num1] 
        str2 = my_string[num1+1:num2]
        str3 = my_string[num2+1:]
        answer = str1+ my_string[num2] + str2 + my_string[num1] + str3
    else:
        str1 = my_string[:num2]
        str2 = my_string[num2+1:num1]
        str3 = my_string[num1+1:]
        answer = str1+ my_string[num1] + str2 + my_string[num2] + str3
    return answer