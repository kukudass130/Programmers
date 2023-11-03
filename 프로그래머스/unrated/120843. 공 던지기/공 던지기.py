def solution(numbers, k):
    answer = 0
    if len(numbers) % 2 == 0:
        numarray = []
        for i in numbers:
            if i % 2 != 0:
                numarray.append(i)
        k = k % len(numarray)
        answer = numarray[k-1]
    else:
        numarray = []
        subarray = []
        for i in numbers:
            if i % 2 != 0:
                numarray.append(i)
            else:
                subarray.append(i)
        numarray = numarray + subarray
        k = k % len(numarray)
        answer = numarray[k-1]
    return answer