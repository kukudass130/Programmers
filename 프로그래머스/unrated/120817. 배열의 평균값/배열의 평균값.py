def solution(numbers):
    answer = 0
    numsum = sum(numbers)
    count = len(numbers)
    answer = numsum / count
    return answer