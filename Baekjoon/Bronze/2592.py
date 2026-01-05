#백준 2592번
#브론즈2
#2026-01-05


import sys
input = sys.stdin.readline

num = []

for _ in range(10):
    n = int(input())
    num.append(n)

print(sum(num)//10)
print(max(set(num), key=num.count))