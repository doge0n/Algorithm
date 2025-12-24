#백준 9395번
#브론 4
#2025-12-24

import sys
input = sys.stdin.readline

T = int(input())

for i in range(1, T+1):
    a, b = map(int, input().split())

    print(f"Case {i}: {a+b}")