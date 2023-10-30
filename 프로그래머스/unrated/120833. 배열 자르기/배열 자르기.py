def solution(numbers, num1, num2):
    answer = []
    for i in numbers[num1: num2+1]:
        answer.append(i)
    return answer