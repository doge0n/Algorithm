## 백준 2562번
# 브론즈3
# 2025-12-27

import sys
input = sys.stdin.readline

list_max = []
for i in range(9):
    n = int(input())
    list_max.append(n)

print(max(list_max))
print(list_max.index(max(list_max)) + 1)
