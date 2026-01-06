# 백준 3460번
# 브론즈3
# 2026-01-06


import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = bin(int(input()))[2:]

    for i in range(len(n)):
        if n[-i-1] == '1':
            print(i, end = " ")