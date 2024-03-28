import sys
input_scale = list(map(int,sys.stdin.readline().split()))
flag = 0
for i in range(1,9):
    if input_scale[i-1] != i:
        flag = 1
        input_scale.reverse()
        for j in range(1,9):
            if input_scale[j-1] != j:
                flag = 2
                break
        break
if flag == 0 : print("ascending")
elif flag == 1 : print("descending")
elif flag == 2 : print("mixed")