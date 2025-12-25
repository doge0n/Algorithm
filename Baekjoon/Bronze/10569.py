#백준 10569번
#브론즈4
#2025-12-25

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    v, e = map(int, input().split())
    print(e-v+2)
