meeting_count = int(input())
meeting_schedule = [list(map(int, input().split())) for _ in range(meeting_count)]
meeting_schedule.sort(key=lambda x: (x[1], x[0]))
end_time = 0
cnt = 0
for meeting in meeting_schedule:
    if meeting[0] >= end_time:
        end_time = meeting[1]
        cnt += 1
print(cnt)