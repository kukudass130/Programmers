def solution(age):
    answer = ''
    newage = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    first = 0
    second = 0
    third = 0
    if age == 1000:
        answer = 'baaa'
        return answer
    if age // 100 > 0:
        first = age //100
        answer = newage[first]
    if age // 10 > 0:
        second = (age - first *100) // 10
        answer = answer + newage[second]
    third = age % 10
    answer = answer + newage[third]
        
    return answer