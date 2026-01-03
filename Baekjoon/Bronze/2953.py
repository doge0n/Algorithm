#백준 2953번
#브론즈3
#2026-01-03

import sys
input = sys.stdin.readline

win_list = []

for _ in range(5):
    n = map(int, input().split())
    n = list(n)

    win_list.append(sum(n))

print(win_list.index(max(win_list))+1, max(win_list))