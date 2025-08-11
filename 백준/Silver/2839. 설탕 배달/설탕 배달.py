N = int(input())
sugar = [5, 3]  # 내림차순 정렬
cnt = 0

while N >= 0:
    if N % 5 == 0:  # 5kg으로 정확하게 나누어 떨어질때
        cnt += N // 5  # 5kg 봉지 개수를 더하고
        print(cnt)  # 총 봉지 개수를 출력
        break  # 정답 찾아서 반복 종료
    N -= 3  # 설탕 무게에서 3kg을 빼고
    cnt += 1  # 3kg 봉지 1개 추가
else: print(-1)  # 5kg + 3kg 형식으로 정확하게 계산이 안되는 경우엔 -1 출력