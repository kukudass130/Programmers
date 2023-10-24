#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int num1, int num2) {
    int answer = 0;
    float a = (float) num1 / (float) num2;
    float b = a*1000;
    answer = (int) b;
    return answer;
}