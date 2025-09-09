T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 1. N개의 새로운 선들이 추가되면서 기존 선들과 비교해야 함
    wires = []  # 기존 선들을 저장
    answer_count = 0  # 실제 교차점 수
    for _ in range(N):
        start, end = map(int, input().split())  # 시작점, 교차점 입력받기
        # 기존 선들과 비교하고 목록에 추가해주기
        # 기존선들과 비교
        for prev_start, prev_end in wires:
            # - 기존 전선보다 시작점 높고 도착점 낮음
            if prev_start < start and prev_end > end:
                answer_count += 1
            # - 기존 전선보다 시작점 낮고 도착점 높음
            if prev_start > start and prev_end < end:
                answer_count += 1
        # 목록에 추가해주기
        wires.append((start, end))
    print(f"#{tc} {answer_count}")