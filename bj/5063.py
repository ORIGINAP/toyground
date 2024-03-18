count = int(input())
r=[]
e=[]
c=[]
for i in range(count):
    r_i, e_i, c_i = map(int,input().split())
    r.append(r_i)
    e.append(e_i)
    c.append(c_i)
for i in range(count):
    before_ad = r[i]
    after_ad = e[i]-c[i]
    if before_ad > after_ad:
        print("do not advertise")
    elif before_ad < after_ad:
        print('advertise')
    elif before_ad == after_ad:
        print('does not matter')