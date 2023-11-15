def solution(str1, str2):
    answer = 0
    len1 = len(str1)
    len2 = len(str2)
    indexlist =[]
    
    for num1 in range(len1- len2 +1):    
        if str2[0] == str1[num1]:
            indexlist.append(num1)
            
    if indexlist == []:
        answer = 2     
    else:
        for i in indexlist:
            strlist = []
            for j in range(len2):
                if str1[i + j] == str2[j]:
                    strlist.append(str2[j])
            if strlist == []:
                answer = 2
            else:
                if ''.join(strlist) == str2:
                    answer = 1
                    return answer
                else:
                    answer = 2
    return answer