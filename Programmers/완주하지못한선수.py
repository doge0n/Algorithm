#프로그래머스 완주하지 못한 선수
#해시 Level1
#2026-01-04

def solution(participant, completion):
    hash_dict = {}
    
    for name in participant:
        if name in hash_dict:
            hash_dict[name] += 1
        else:
            hash_dict[name] = 1
    print(f"test-1 {hash_dict}")
            
    for name in completion:
        hash_dict[name] -= 1
    print(f"test-2 {hash_dict}")

    for name in hash_dict:
        if hash_dict[name] > 0:
            return name