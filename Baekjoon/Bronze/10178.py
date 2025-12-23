#백준 10178번
#브론즈 3
#25-12-23

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    c, v = map(int, input().split())


    print(f"You get {c//v} piece(s) and your dad gets {c%v} piece(s).")