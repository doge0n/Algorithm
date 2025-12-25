#백준 2921번
#브론즈 3 - 단순구현
#2025-12-25

import sys
input = sys.stdin.readline

n = int(input())

total = 0

for i in range(n+1):
    for j in range(i, n+1):
        total += i+j

print(total)