import math

def solution(array):
    answer = 0
    array.sort()
    middle = math.ceil(len(array)/2)
    answer = array[middle -1]
    return answer