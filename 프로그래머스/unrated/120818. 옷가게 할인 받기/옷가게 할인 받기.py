def solution(price):
    answer = 0
    if price >= 500000:
        price = price * 0.8
    elif price >= 300000:
    	price = price * 0.9
    elif price >= 100000:
        price = price * 0.95
    answer = int(price)
    return answer