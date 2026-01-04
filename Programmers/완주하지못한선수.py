#프로그래머스 완주하지 못한 선수
#해시 Level1
#2026-01-04

#풀이1

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
        

#풀이2

import collections

def solution(participant, completion):
    # 1. 각 명단의 개수를 세어주는 Counter 객체를 만든다
    # 2. Counter끼리는 뺄셈이 가능하며, 결과로 남은 객체에서 키값을 가져온다
    answer = collections.Counter(participant) - collections.Counter(completion)
    
    # 3. 뺄셈 결과 남은 첫 번째 이름을 반환
    return list(answer.keys())[0]