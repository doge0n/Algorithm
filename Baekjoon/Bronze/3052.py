#백준 3052번
#브론즈2
#2026-01-04

import sys
input = sys.stdin.readline

result_list = []

for i in range(10):
    N = int(input())

    S = N % 42
    if S not in result_list:
        result_list.append(S)

print(len(result_list))
