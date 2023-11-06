def solution(numbers):
    answer = 0
    x = 0
    y = 0
    for i in numbers:
        if i > x:
            x = i
    numbers.remove(x)
    for j in numbers:
        if j > y:
            y = j
    answer = x * y
    return answer