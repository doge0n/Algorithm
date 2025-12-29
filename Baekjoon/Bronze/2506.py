#백준 2506번
#브론즈3
#2025-12-29

import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

score = 0
cnt = 0
for i in num:
    if i == 1:
        cnt += 1
        score += cnt
    else:
        cnt = 0

print(score)
