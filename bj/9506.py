val = []

while(1):
    val_i = int(input())
    if(val_i != -1):
        val.append(val_i)
    else:
        break
def check_divisor(num):
    divisor_o = []
    for i in range(num - 1):
        if(num%(i+1)) == 0:
            divisor_o.append(i+1)
    return divisor_o

def show_perfect():
    val_divisor = []
    count = 0
    for i in val:
        val_divisor.append(check_divisor(i))
        if i == sum(val_divisor[count]):
            print(f'{i} = ' + ' + '.join(map(str,val_divisor[count])))
        else:
            print(f'{i} is NOT perfect.')
        count += 1
show_perfect()