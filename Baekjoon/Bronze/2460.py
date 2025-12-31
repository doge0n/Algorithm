#백준 2460번
#브론즈3
#2025-12-31

import sys
input = sys.stdin.readline

sum_result = 0
sum_list = []

for i in range(10):

    n, m = map(int, input().split())
    sum_result = sum_result - n + m
    sum_list.append(sum_result)


print(max(sum_list))


