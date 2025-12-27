#백준 2501번
#브론즈3
#2025-12-27

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

list_divisors = []

for i in range(1, n+1):
    if n % i == 0:
        list_divisors.append(i)

if len(list_divisors) < k:
    print(0)
else:
    print(list_divisors[k-1])


