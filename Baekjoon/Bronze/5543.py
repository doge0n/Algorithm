#백준 5543번
#브론즈4
#2026-01-08

import sys
input = sys.stdin.readline

burger = []
drink = []

for i in range(5):

    if i < 3:
        burger.append(int(input()))
    else:
        drink.append(int(input()))

result = min(burger) + min(drink) - 50

print(result)
    