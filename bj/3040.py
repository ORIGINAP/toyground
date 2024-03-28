scale = [0,1,2,3,4,5,6]
input_val = []
for i in range(9):
    input_val.append(int(input()))

def show_val(l):
    for i in range(7):
        print(l[i])

def up_scale(n):
    if (n+2) <= scale[n]:
        scale[n] = up_scale(n-1)
    else:
        scale[n] += 1
    return scale[n] + 1
flag = 0
while True:
    if flag != 0:
        up_scale(6)
    calc_list = []
    for i in range(7):
        calc_list.append(input_val[scale[i]])
    if sum(calc_list) == 100:
        show_val(calc_list)
        break
    if scale[0] == 2:
        break
    flag += 1