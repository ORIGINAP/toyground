import sys
listen_not,see_not = map(int,sys.stdin.readline().split())
listen_not_l = []
see_not_l = []
for l in range(listen_not):
    l_i = sys.stdin.readline().rstrip()
    listen_not_l.append(l_i)
for s in range(see_not):
    s_i = sys.stdin.readline().rstrip()
    see_not_l.append(s_i)
lin = set(listen_not_l)
sin = set(see_not_l)
lin_sin = list(lin & sin)
lin_sin.sort()
print(len(lin_sin))
for i in lin_sin: print(i)