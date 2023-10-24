import math
#import fractions

def solution(numer1, denom1, numer2, denom2):
    answer = []
    #주어진 분수들이 기약분수인지 판별
    if(math.gcd(numer1, denom1) != 1):
        gcd = math.gcd(numer1, denom1)
        numer1 = numer1 //gcd
        denom1 = denom1 // gcd
        print(numer1, denom1)
    if(math.gcd(numer2, denom2) != 1):
        gcd = math.gcd(numer2, denom2)
        numer2 = numer2 //gcd
        denom2 = denom2 // gcd
    #분수를 더하고 기약분수로 만들기 (1/ 4 / 13/ 4)
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    Lgcd = math.gcd(numer, denom)
    answer = [numer // Lgcd, denom // Lgcd]
    return answer
