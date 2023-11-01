def solution(hp):
    answer = 0
    captain = hp //5
    soldier = hp % 5 //3
    worker = hp % 5 %3
    answer = captain + soldier + worker
    return answer