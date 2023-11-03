def solution(numbers, direction):
    answer = []
    if direction == "left":
        tmp = numbers.pop(0)
        numbers.append(tmp)
        answer = numbers
    else:
        tmp = [numbers.pop()]
        tmp.extend(numbers)
        answer = tmp
    return answer