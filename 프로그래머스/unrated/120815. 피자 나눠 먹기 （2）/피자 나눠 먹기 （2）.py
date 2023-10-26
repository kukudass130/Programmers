def solution(n):
    answer = 0
    rest = 6 % n
    count = 1
    while rest !=0:
        count = count +1
        rest = 6 * count % n
    answer = count
    return answer