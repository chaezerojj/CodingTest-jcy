# 종료조건 : 12달을 모두 고려
# 가지의 수 : 4개 (1일, 1달, 3달, 1년)
def recur(month, total_cost):
    global min_answer
    if month > 12:
        if total_cost < min_answer:
            min_answer = total_cost
        return

    # 1일권으로 다 사는 경우
    recur(month + 1, total_cost + (days[month] * cost_day))
    # 1달권으로 다 사는 경우
    recur(month + 1, total_cost + cost_month)
    # 3달권으로 다 사는 경우
    recur(month + 3, total_cost + cost_month3)
    # 1년 이용권으로 사는 경우
    recur(month + 12, total_cost + cost_year)




T = int(input())
for tc in range(1, T + 1):
    # 이용권 가격들 (1일, 1달, 3달, 1년)
    cost_day, cost_month, cost_month3, cost_year = map(int, input().split())
    # 12개월 이용 계획
    days = [0] + list(map(int, input().split()))
    min_answer = float('inf')
    recur(1, 0)
    print(f"#{tc} {min_answer}")