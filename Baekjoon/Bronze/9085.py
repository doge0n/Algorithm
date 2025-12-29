#백준 9085번
#브론즈3번
#2025-12-28

import sys
input = sys.stdin.readline

T = int(input())


for _ in range(T):
    N = int(input())

    sum_list = [int(x) for x in input().split()]
    print(sum(sum_list))
