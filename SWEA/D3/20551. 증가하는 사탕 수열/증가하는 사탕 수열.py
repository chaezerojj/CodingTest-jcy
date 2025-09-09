T = int(input())
for tc in range(1, T + 1):
    # 3개정도는 따로 받기
    A, B, C = map(int, input().split())
    eat_count = 0

    # 불가능한 케이스 먼저 지우기
    if A < 1 or B < 2 or C < 3:
        print(f"#{tc} -1") # 안되는건 -1 출력
        continue

    # B상자 = C상자 - 1
    # - B가 C보다 크거나 같을 때만
    if B >= C:
        eat_count += B - (C - 1)
        B = C - 1

    # A상자 = B상자 - 1
    # - A가 B보다 크거나 같을 때만
    if A >= B:
        eat_count += A - (B - 1)
        A = B - 1

    print(f"#{tc} {eat_count}")