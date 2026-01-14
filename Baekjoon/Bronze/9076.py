#백준 9076번
#브론즈2
#2026-01-14


import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    arr = list(map(int, input().split()))
    result = sorted(arr)
    result.pop(0)
    result.pop(-1)

    if result[-1] - result[0] >= 4:
        print("KIN")
    else:
        print(sum(result))
