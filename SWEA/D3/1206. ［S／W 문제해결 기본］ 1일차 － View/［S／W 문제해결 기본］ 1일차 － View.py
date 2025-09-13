for tc in range(1, 11):
    N = int(input())
    height = list(map(int, input().split()))
    view = 0

    # 앞 0 0 뒤 0 0 제외하고 범위 설정
    for b in range(2, N - 2):
        # 조망권 범위: 양 옆 각 2칸씩 확보되어야 함
        # - 앞 2칸, 뒤 3칸(중간 1칸포함)
        check_view = height[b - 2:b + 3]
        # 원본 복사
        # 원본으로는 가운데 건물 확인. 복사본으로는 가장 높은 건물, 두번째로 높은 건물 확인
        check_view_cp = check_view[:]
        # 복사본 내림차순 정렬
        check_view_cp.sort(reverse=True)
        # 현재 건물이 구간에서 가장 높은 건물인지 확인
        if check_view[2] == check_view_cp[0]:
            # 현재 건물 높이 - 주변에서 가장 높은 건물 높이 = 조망권 확보 층수
            view += check_view_cp[0] - check_view_cp[1]
    print(f"#{tc} {view}")