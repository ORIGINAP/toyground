h,m = map(int,input().split())
if h==0: h=24
time = m + h*60
alarm_t = time - 45
h_o = int(alarm_t/60)
h_o = h_o if h_o < 24 else 0
print(f'{h_o} {alarm_t%60}')