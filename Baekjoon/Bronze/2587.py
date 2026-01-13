#백준 2587번
#브론즈2
#2026-01-13


import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(5)]


print(sum(arr)//5)
print(sorted(arr)[2])
