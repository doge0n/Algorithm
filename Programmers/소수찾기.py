from itertools import permutations
# import math

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5)+ 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    
    numbers = list(numbers)
    print(numbers)
    made = set()
    
    for i in range(1, len(numbers) +1):
        for j in permutations(numbers, i):
            made.add(int(''.join(j)))
            print(made)
    
    cnt = 0
    for x in made:
        if is_prime(x):
            cnt += 1
    
    print(cnt)
    return cnt

