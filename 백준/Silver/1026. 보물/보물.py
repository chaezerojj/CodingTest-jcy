N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

min_s = 0 
for i in range(N):
    min_s += min(A) * max(B)
    A.pop(A.index(min(A))) # 계산한 값은 배열에서 빼기
    B.pop(B.index(max(B)))
print(min_s)