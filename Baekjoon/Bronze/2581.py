#백준 2581번
#브론즈2
#2025-12-26

import sys
input = sys.stdin.readline

M = int(input())
N = int(input())

list = []

for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        list.append(i)

if len(list) == 0:
    print(-1)
else:
    print(sum(list))
    print(min(list))
