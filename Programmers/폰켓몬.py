#프로그래머스 폰켓몬
#Level 1
#2026-01-04

#풀이1 - 직접품

def solution(nums):
    hash_dict = {}
    
    a = len(nums)//2
    
    for name in nums:
        if name in hash_dict:
            hash_dict[name] += 1
        else:
            hash_dict[name] = 1
    
    b = len(list(hash_dict.keys()))
    
    return min(a,b)
        
#풀이2

def solution(nums):
    a = len(nums)//2
    b = len(set(nums))
        
    return min(a, b)
    