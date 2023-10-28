def solution(num_list):
    answer = []
    eve = 0
    odd = 0
    for i in num_list: 
        if i % 2 ==0:
            eve = eve +1
        else:
            odd = odd +1
    answer = [eve, odd]
    return answer