S, P = map(int, input().split())           # dna 문자열 길이 S, 비밀번호로 사용할 부분문자열 길이 P
dna_str = input().strip()                  # 임의로 만든 dna 문자열
min_str = list(map(int, input().split()))  # 부분문자열에 포함되어야 할 A, C, G, T의 최소 개수
str_cnt = [0, 0, 0, 0]                     # dna 문자열에 A, C, G, T 각각 몇개인지 세어서 담을 배열 초기화
result = 0                                 # 만들 수 있는 비밀번호 종류 수(결과값)

def str_idx(str):
    # A, C, G, T를 인덱스 0 ~ 3에 각각 몇개 있는지 담음
    if str == 'A': return 0
    elif str == 'C': return 1
    elif str == 'G': return 2
    else: return 3

# 길이 P만큼 배열을 돌면서,
# dna 문자열의 각 문자들의 개수를 str_cnt 배열에 각각 증가시키면서 담음
for i in range(P):
    str_cnt[str_idx(dna_str[i])] += 1

# dna 문자열 입력받은 값의 각 개수들이 각 문자열 최소 개수 조건에 만족하는지 확인
def cnt_check():
    for i in range(4):
        if str_cnt[i] < min_str[i]:
            return False
    return True

# 윈도우 검사: 최소 개수 조건 만족하면 사용할 수 있는 비밀번호로 result 카운트
if cnt_check(): result += 1

# 슬라이딩 윈도우
# 앞에서부터 한 칸씩 이동하면서 하나씩 검사
for i in range(P, S):  # 초기 윈도우는 이미 계산했으니 그 다음부터 범위를 돌면서 확인
    # 이전 윈도우에서 빠져나가는 문자 처리
    str_cnt[str_idx(dna_str[i - P])] -= 1
    # 새로 들어오는 문자 처리
    str_cnt[str_idx(dna_str[i])] += 1

    # 현재 윈도우 검사: 조건 만족 시 result 카운트
    if cnt_check(): result += 1

print(result)