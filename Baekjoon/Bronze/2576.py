#백준 2576번
#브론즈3
#2025-12-30

import sys
input = sys.stdin.readline

dp = []

for _ in range(7):
    num = int(input())

    if num % 2 == 0:
        continue
    else:
        dp.append(num)

if len(dp) == 0:
    print(-1)
else:
    print(sum(dp))
    print(min(dp))

