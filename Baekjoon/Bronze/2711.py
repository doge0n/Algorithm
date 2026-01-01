#백준 2711번
#브론즈 2
#2026-01-01

import sys
input = sys.stdin.readline


T = int(input())

for i in range(T):
    N, S = input().split()
    N = int(N)
    S = list(S)
    S.pop(N-1)
    print("".join(S))
    