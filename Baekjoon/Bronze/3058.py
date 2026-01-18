# 백준 3058번
# 브론즈3
# 2026-01-18


import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    jjacksu = []
    arr = list(map(int, input().split()))

    for i in arr:
        if i % 2 == 0:
            jjacksu.append(i)
    
    print(sum(jjacksu))
    print(min(jjacksu))
    
