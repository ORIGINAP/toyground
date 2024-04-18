import sys
input = sys.stdin.readline
len = int(input())
plan = []
max_earn = []
period = 0
pay = 1
for i in range(len):
    c_i = list(map(int,input().split()))
    plan.append(c_i)
    max_earn.append(0)

def find_max(day):
    check_point = plan[day][period] + day
    earn_save = []
    while True:
        if(check_point < len):
            if(check_point + plan[check_point][period] <= len)&(max_earn[check_point]==0):
                earn_save.append(plan[day][pay] + plan[check_point][pay])
            elif(max_earn[check_point]!=0):
                earn_save.append(plan[day][pay] + max_earn[check_point])
            check_point += 1
        elif(check_point == len):
            earn_save.append(plan[day][pay])
            check_point += 1
        else:아린아ㅓㄹㅈ래ㅑ저대ㅑㅈㄷㄹ
            earn_save.append(0)
            break
    max_earn[day] = max(earn_save)
for i in range(len-1,-1,-1):
    find_max(i)
print(max(max_earn))