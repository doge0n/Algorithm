import math

def solution(brown, yellow):
    # 중앙(노란색) 크기를 (a, b)라고 두면 a*b = yellow
    # 전체 카펫은 (a+2, b+2) (테두리 1줄이므로 양쪽으로 +2)
    # brown = 전체 - 중앙 = (a+2)(b+2) - ab = 2a + 2b + 4

    for a in range(1, int(math.isqrt(yellow)) + 1):
        if yellow % a != 0:
            continue
        b = yellow // a  # a*b = yellow

        # 테두리(갈색) 개수 조건 확인
        if 2 * a + 2 * b + 4 == brown:
            w, h = b + 2, a + 2  # w >= h 되도록 b를 가로로
            if w < h:
                w, h = h, w
            return [w, h]
