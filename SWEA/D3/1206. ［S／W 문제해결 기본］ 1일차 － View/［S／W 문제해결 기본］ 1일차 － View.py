for tc in range(1, 11):
    N = int(input())
    heights = list(map(int, input().split()))
    view = 0

    for i in range(2, N - 2):
        max_height = max(heights[i - 2], heights[i - 1], heights[i + 1], heights[i + 2])
        if heights[i] > max_height:
            # 조망권 세대 수 = 현재 건물 높이 - 최대 건물 높이
            view += heights[i] - max_height
    print(f"#{tc} {view}")