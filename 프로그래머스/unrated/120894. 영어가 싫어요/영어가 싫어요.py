def solution(numbers):
    answer = 0
    numtmp = ''
    strnum =''
    numberlist = {"zero": 0, "one": 1, "two" : 2, "three" : 3, "four":4, "five":5, "six": 6, "seven": 7, "eight": 8, "nine" : 9}
    for i in numbers:
        numtmp = numtmp + i
        if numtmp in numberlist.keys():   
            index = numberlist.get(numtmp)
            strnum = strnum + str(index)
            numtmp = ''
    answer = int(strnum)
    return answer