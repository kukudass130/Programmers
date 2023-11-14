def solution(num, k):
    answer = 0
    numlist = []
    for i in str(num):
        numlist.append(i)
    for j in range(len(numlist)):
        if int(numlist[j]) == k:
            answer = j +1
            break
        else:
            answer = -1
    return answer