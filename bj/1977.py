import math
M = int(input())
N = int(input())
save_pow_val = []

for i in range(int(N/2)):
    pow_val = math.pow(i,2)
    if pow_val >= M and pow_val <= N:
        save_pow_val.append(pow_val)
if save_pow_val != []:
    print(int(sum(save_pow_val)))
    print(int(min(save_pow_val)))
else:
    print('-1')