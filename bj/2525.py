h,m = map(int,input().split())
need_time = int(input())
time = m + h*60
alarm_t = time + need_time
h_o = int(alarm_t/60)%24
print(f'{h_o} {alarm_t%60}')